from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from core.database import engine

Base = declarative_base()

class Produto(Base):
    
    ___tablename__ = "produto"
    
    id = Column(Integer, primary_key=True, autoincrement="auto")
    gtin = Column(String, unique=True, nullable=False)
    nome = Column(String(255), unique=True, nullable=False)
    descricao = Column(String(500), unique=False, nullable=True)
    
    