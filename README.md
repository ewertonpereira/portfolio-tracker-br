# 📈 Portfolio Tracker BR

A REST API built with FastAPI that fetches real-time stock prices 
from B3 and manages your investment portfolio.

## 🚀 Features
- Full CRUD REST API with FastAPI
- Real-time stock prices via brapi.dev
- Secure token handling with environment variables
- Portfolio data stored in CSV

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
   ticker,amount
   PETR4,10
   ITUB4,8

5. Run the API:
   uvicorn api:app --reload

## 📡 Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /portfolio | Returns all stocks and total value |
| GET | /portfolio/{ticker} | Returns a specific stock |
| POST | /portfolio | Adds a new stock |
| PUT | /portfolio/{ticker} | Updates stock amount |
| DELETE | /portfolio/{ticker} | Removes a stock |

## 📊 Example response — GET /portfolio
{
  "portfolio": [
    {
      "ticker": "PETR4",
      "amount": 10,
      "price": 37.64,
      "total_value": 376.40
    }
  ],
  "total": 376.40
}