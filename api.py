from fastapi import FastAPI
from main import load_wallet, get_stock_price
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

app = FastAPI()

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
            'quantidade': amount,
            'preco': price,
            'valor_total': round(value)
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
    