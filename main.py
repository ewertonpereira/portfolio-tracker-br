import csv
import requests
from dotenv import load_dotenv
import os

URL = 'https://brapi.dev/api/v2/stocks/quote'

load_dotenv()
TOKEN = os.getenv('TOKEN')

def load_wallet(filename):
    wallet = {}
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            wallet[row['ticker']] = int(row['amount'])
    return wallet

def save_wallet(wallet: dict, filename:str):
    with open(filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['ticker', 'amount'])
        writer.writeheader()
        for ticker, amount in wallet.items():
            writer.writerow({'ticker': ticker, 'amount': amount})

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
