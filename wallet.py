import csv
import requests
from dotenv import load_dotenv
import os

URL = 'https://brapi.dev/api/v2/stocks/quote'

load_dotenv()
TOKEN = os.getenv('TOKEN')

def load_wallet(file_name):
    wallet = {}
    with open(file_name) as f:
        reader = csv.DictReader(f)
        for row in reader:
            wallet[row['ticker']] = int(row['quantidade'])
    return wallet

def get_stock_price(symbol, token):
    params = {
            'symbols': symbol,
            'token': token
        }
    
    r = requests.get(URL, params=params)
    data_json = r.json()
    
    if not data_json.get('results'):
        print(f'{symbol}: erro ao buscar preço')
        return None

    return data_json['results'][0]['data']['regularMarketPrice']

wallet = load_wallet('wallet.csv')

def calculate_portfolio(wallet, token):
    total_price = 0

    for symbol, amount in wallet.items():
        price = get_stock_price(symbol, token)
        if price is None:
            continue

        sum_stock_price = amount * price
        total_price += sum_stock_price
        print(f'{symbol}: {amount} cotas x R${price:.2f} = R${sum_stock_price:.2f}')

    print(f'\nValor total da carteira: R${total_price:.2f}')

calculate_portfolio(wallet, TOKEN)