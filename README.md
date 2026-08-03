# 📈 Portfolio Tracker BR

A Python API that fetches real-time stock prices from B3 
and calculates the total value of your portfolio.

## 🚀 Features
- REST API built with FastAPI
- Real-time stock prices via brapi.dev
- Get full portfolio or individual stock data
- Reads portfolio from CSV file
- Secure token handling with environment variables

## 🛠️ Technologies
- Python 3
- FastAPI
- Uvicorn
- Requests
- python-dotenv

## ⚙️ How to use

1. Clone the repository
2. Install dependencies:
   pip install -r requirements.txt

3. Create a `.env` file:
   TOKEN=your_brapi_token_here

4. Edit `wallet.csv` with your stocks:
   ticker,quantidade
   PETR4,10
   ITUB4,8

5. Run the API:
   uvicorn api:app --reload

## 📡 Endpoints

GET /portfolio
→ Returns all stocks and total portfolio value

GET /portfolio/{ticker}
→ Returns data for a specific stock
→ Example: /portfolio/PETR4

## 📊 Example response
{
  "portfolio": [
    {"ticker": "PETR4", "quantidade": 10, "preco": 37.64, "valor_total": 376.40}
  ],
  "total": 4979.81
}