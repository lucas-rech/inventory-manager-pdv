from sqlalchemy.orm import Session
from models.product import Product

class ProductRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def create(self, name: str, gtin: str, quantity: int, price: float) -> Product:
        product = Product(name=name, gtin=gtin, quantity=quantity, price=price)
                    
        self.db.add(product)
        self.db.commit()
        self.db.refresh(product)
        return product
    
    
    def get_by_id(self, product_id: int) -> Product | None:
        return self.db.query(Product).filter(Product.id == product_id).first()
    
    def get_all(self) -> list[Product]:
        return self.db.query(Product).all()
    
    def update_quantity(self, product_id: int, new_quantity: int) -> Product | None:
        product = self.get_by_id(product_id)
        if not product:
            return None
        product.quantity = new_quantity
        self.db.commit()
        self.db.refresh(product)
        return product
    
    
    def delete(self, product_id: int) -> bool:
        product = self.get_by_id(product_id)
        if not product:
            return False
        self.db.delete(product)
        self.db.commit()
        return True

        
    