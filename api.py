import os
from fastapi import FastAPI
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

@app.get('/portfolio')
def get_portfolio():
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
def get_one_stock(ticker: str):
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
def create_stock(stock: StockInput):
    existing = get_stock(stock.ticker)
    if existing:
        return {'error': f'{stock.ticker} já existe na carteira'}
    add_stock(stock.ticker, stock.amount)
    return {'message': f'{stock.ticker} adicionado com sucesso!'}

@app.put('/portfolio/{ticker}')
def edit_stock(ticker: str, stock: StockUpdate):
    existing = get_stock(ticker)
    if existing is None:
        return {'error': f'{ticker} não encontrado na carteira'}
    update_stock(ticker, stock.amount)
    return {'message': f'{ticker} atualizado com sucesso!', 'amount': stock.amount}

@app.delete('/portfolio/{ticker}')
def remove_stock(ticker: str):
    existing = get_stock(ticker)
    if existing is None:
        return {'error': f'{ticker} não encontrado na carteira'}
    delete_stock(ticker)
    return {'message': f'{ticker} removido com sucesso!'}