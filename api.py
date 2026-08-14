import os
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from auth import create_token, verify_password, verify_token
from users import create_user, get_user
from dotenv import load_dotenv
from pydantic import BaseModel
from crud import get_all_stocks, get_stock, add_stock, update_stock, delete_stock
from main import get_stock_price

load_dotenv()
TOKEN = os.getenv('TOKEN')

app = FastAPI()

class StockInput(BaseModel):
    ticker: str
    amount: int

class StockUpdate(BaseModel):
    amount: int

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='auth/login')

def get_current_user(token: str = Depends(oauth2_scheme)):
    email = verify_token(token)
    if email is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Token inválido ou expirado'
        )
    return email

@app.post('/auth/register')
def register(form: OAuth2PasswordRequestForm=Depends()):
    user = create_user(form.username, form.password)
    if user is None:
        return{ 'error': 'Email já cadastrado'}
    return {'message': 'Usuário criado com sucesso!'}

@app.post('/auth/login')
def login(form: OAuth2PasswordRequestForm=Depends()):
    user = get_user(form.username)
    if user is None or not verify_password(form.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Email ou senha incorretos'
        )
    token = create_token({'sub': form.username})
    return {'access_token': token, 'token_type': 'bearer'}

@app.get('/portfolio')
def get_portfolio(current_user: str = Depends(get_current_user)):
    stocks = get_all_stocks()
    result = []
    total = 0

    for stock in stocks:
        price = get_stock_price(stock.ticker, TOKEN)
        if price is None:
            continue
        value = stock.amount * price
        total += value
        result.append({
            'ticker': stock.ticker,
            'amount': stock.amount,
            'price': price,
            'total_value': round(value, 2)
        })

    return {'portfolio': result, 'total': round(total, 2)}

@app.get('/portfolio/{ticker}')
def get_one_stock(ticker: str, current_user: str = Depends(get_current_user)):
    stock = get_stock(ticker)
    if stock is None:
        return {'error': f'{ticker} não encontrado na carteira'}
    price = get_stock_price(ticker, TOKEN)
    if price is None:
        return {'error': f'Erro ao buscar preço de {ticker}'}
    return {
        'ticker': stock.ticker,
        'amount': stock.amount,
        'price': price,
        'total_value': round(stock.amount * price, 2)
    }

@app.post('/portfolio')
def create_stock(stock: StockInput, current_user: str = Depends(get_current_user)):
    existing = get_stock(stock.ticker)
    if existing:
        return {'error': f'{stock.ticker} já existe na carteira'}
    add_stock(stock.ticker, stock.amount)
    return {'message': f'{stock.ticker} adicionado com sucesso!'}

@app.put('/portfolio/{ticker}')
def edit_stock(ticker: str, stock: StockUpdate, current_user: str = Depends(get_current_user)):
    existing = get_stock(ticker)
    if existing is None:
        return {'error': f'{ticker} não encontrado na carteira'}
    update_stock(ticker, stock.amount)
    return {'message': f'{ticker} atualizado com sucesso!', 'amount': stock.amount}

@app.delete('/portfolio/{ticker}')
def remove_stock(ticker: str, current_user: str = Depends(get_current_user)):
    existing = get_stock(ticker)
    if existing is None:
        return {'error': f'{ticker} não encontrado na carteira'}
    delete_stock(ticker)
    return {'message': f'{ticker} removido com sucesso!'}