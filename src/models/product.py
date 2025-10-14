from sqlalchemy import Column, Integer, String, Float
from core.database import Base

class Product(Base):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), index=True)
    gtin = Column(String(14), index=True, unique=True)
    quantity = Column(Integer, index=True)
    price = Column(Float, index=True)
    
    def __init__(self, name: str, gtin: str, quantity: int = 0, price: float = 0):
        self.name = name
        self.gtin = gtin
        self.quantity = quantity
        self.price = price
        
    def __repr__(self):
        return f"Product:(id={self.id}, name={self.name}, gtin={self.gtin}, quantity={self.quantity}, price={self.price})"