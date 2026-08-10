from database import get_session, Stock

def get_all_stocks():
    with get_session() as session:
        return session.query(Stock).all()

def get_stock(ticker:str):
    with get_session() as session:
        return session.query(Stock).filter(Stock.ticker == ticker).first()

def add_stock(ticker:str, amount:int):
    with get_session() as session:
        stock = Stock(ticker=ticker, amount=amount)
        session.add(stock)
        session.commit()

def update_stock(ticker:str, amount:int):
    with get_session() as session:
        stock = session.query(Stock).filter(Stock.ticker == ticker).first()
        if stock:
            stock.amount = amount
            session.commit()

def delete_stock(ticker:str):
    with get_session() as session:
        stock = session.query(Stock).filter(Stock.ticker == ticker).first()
        if stock:
            session.delete(stock)
            session.commit()