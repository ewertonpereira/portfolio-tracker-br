import os
from fastapi import FastAPI
from main import load_wallet, save_wallet,  get_stock_price
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()
TOKEN = os.getenv('TOKEN')

app = FastAPI()

class Stock(BaseModel):
    ticker: str
    amount: int

@app.post('/portfolio')
def add_stock(stock: Stock):
    wallet = load_wallet('wallet.csv')
    if stock.ticker in wallet:
        return {'error':f'{stock.ticker} já existe na carteira.'}

    wallet[stock.ticker] = stock.amount
    save_wallet(wallet, 'wallet.csv')

    return {'message': f'{stock.ticker} adicionado com sucesso!'}

@app.get('/portfolio')
def get_portfolio():
    wallet = load_wallet('wallet.csv')
    result = []
    total = 0

    for symbol, amount in wallet.items():
        price = get_stock_price(symbol, TOKEN)
        if price is None:
            continue

        value = amount * price
        total += value
        result.append({
            'ticker':symbol,
            'amount': amount,
            'price': price,
            'total_value': round(value)
        })

    return {
        'portfolio': result,
        'total': round(total, 2)
    }

@app.get('/portfolio/{ticker}')
def get_stock(ticker:str):
    wallet = load_wallet('wallet.csv')
  
    amount = wallet.get(ticker)
    if amount is None:
        return {'error': f'{ticker} não encontrado na carteira'}

    price = get_stock_price(ticker, TOKEN)
    if price is None:
        return {'error': f'Erro ao buscar preço de {ticker}'}

    return {
            'ticker':ticker,
            'quantidade': amount,
            'preco': price,
            'valor_total': round(amount * price, 2)
        }

