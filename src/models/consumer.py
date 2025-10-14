from sqlalchemy import Column, Integer, String
from core.database import Base

class Consumer:
    __tablename__ = "consumers"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50), index=True)
    last_name = Column(String(100), index=True)
    cpf = Column(String(11), index=True, unique=True)
    email = Column(String, index=True, unique=True)