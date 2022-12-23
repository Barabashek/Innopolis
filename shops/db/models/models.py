from datetime import datetime
from sqlalchemy import (Column, Integer, String, ForeignKey, Float, DateTime)
from sqlalchemy.orm import relationship, backref
from db.config import Base


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), unique=True, nullable=False)
    price = Column(Float)

class Store(Base):
    __tablename__ = 'stores'

    id = Column(Integer, primary_key=True, autoincrement=True)
    address = Column(String(50), nullable=False)

class Sale(Base):
    __tablename__ = 'sales'

    id = Column(Integer, primary_key=True, autoincrement=True)
    sale_time = Column(DateTime, nullable=False, default=datetime.now())
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    product = relationship('Product', backref=backref('sale', uselist=False))
    store_id = Column(Integer, ForeignKey('stores.id'), nullable=False)
    store = relationship('Store', backref=backref('sale', uselist=False))
