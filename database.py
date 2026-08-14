from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import DeclarativeBase, Session

engine = create_engine('sqlite:///portfolio.db')

class Base(DeclarativeBase):
    pass

class Stock(Base):
    __tablename__ = 'stocks'

    id = Column(Integer, primary_key=True)
    ticker = Column(String, unique=True, nullable=False)
    amount = Column(Integer, nullable=False)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

Base.metadata.create_all(engine)

def get_session():
    return Session(engine)