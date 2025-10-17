from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite://database.db', echo=True)

SessionLocal = sessionmaker(bind=engine)


def get_session():
    return SessionLocal()