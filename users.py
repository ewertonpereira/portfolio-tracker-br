from database import get_session, User
from auth import hash_password

def create_user(email:str, password:str):
    with get_session() as session:
        existing = session.query(User).filter(User.email == email).first()
        if existing:
            return None

        user = User(email=email, password=hash_password(password))
        session.add(user)
        session.commit()
        return user

def get_user(email:str):
    with get_session() as session:
        return session.query(User).filter(User.email == email).first()