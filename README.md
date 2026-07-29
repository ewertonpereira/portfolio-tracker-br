# 📈 Portfolio Tracker BR

A Python script that fetches real-time stock prices from B3 
and calculates the total value of your portfolio.

## 🚀 Features
- Reads portfolio from a CSV file
- Fetches real-time prices via brapi.dev API
- Calculates total value per stock and overall portfolio

## 🛠️ Technologies
- Python 3
- Requests
- python-dotenv
- brapi.dev API

## ⚙️ How to use

1. Clone the repository
2. Install dependencies:
   pip install -r requirements.txt

3. Create a `.env` file with your brapi.dev token:
   TOKEN=your_token_here

4. Edit `wallet.csv` with your stocks:
   ticker,quantidade
   PETR4,132
   ITUB4,21

5. Run:
   python main.py

## 📊 Example output
PETR4: 132 cotas x R$37.64 = R$4.968,48
BBSE3: 85 cotas x R$38.15 = R$3.242,75

Valor total da carteira: R$17.825,14