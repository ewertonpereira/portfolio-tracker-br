# 📈 Portfolio Tracker BR

A REST API built with FastAPI that fetches real-time stock prices 
from B3 and manages your investment portfolio.

## 🚀 Features
- Full CRUD REST API with FastAPI
- Real-time stock prices via brapi.dev
- SQLite database with SQLAlchemy ORM
- Secure token handling with environment variables

## 🛠️ Technologies
- Python 3
- FastAPI
- Uvicorn
- SQLAlchemy
- Requests
- python-dotenv

## ⚙️ How to use

1. Clone the repository
2. Install dependencies:
   pip install -r requirements.txt

3. Create a `.env` file:
   TOKEN=your_brapi_token_here

4. Run the API:
   uvicorn api:app --reload

5. Access the auto-generated docs:
   http://localhost:8000/docs

## 📡 Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /portfolio | Returns all stocks and total value |
| GET | /portfolio/{ticker} | Returns a specific stock |
| POST | /portfolio | Adds a new stock |
| PUT | /portfolio/{ticker} | Updates stock amount |
| DELETE | /portfolio/{ticker} | Removes a stock |

## 📊 Example response — GET /portfolio
```json
{
  "portfolio": [
    {
      "ticker": "PETR4",
      "amount": 132,
      "price": 42.06,
      "total_value": 5551.92
    }
  ],
  "total": 5551.92
}
```

## 🗂️ Project structure

```
portfolio-tracker-br/
├── api.py          → FastAPI endpoints
├── crud.py         → database operations
├── database.py     → SQLAlchemy models and connection
├── main.py         → stock price fetching
├── .env            → token (not versioned)
├── .gitignore
├── requirements.txt
└── README.md
```

## 📌 Branches
- `main` → v2 — SQLite + SQLAlchemy
- `feature/database` → v2 development branch
- Older CSV version available in git history