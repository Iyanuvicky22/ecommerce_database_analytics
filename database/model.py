"""
Author: Ajeyomi Adedoyin Samuel
Email: adedoyinsamuel25@gmail.com
Date: 07-03-2025


https://www.codearmo.com/python-tutorial/sql-alchemy-foreign-keys-and-relationships
https://docs.sqlalchemy.org/en/20/orm/basic_relationships.html
https://stackoverflow.com/questions/6017895/select-table-from-other-schema
https://thegirlsynth.hashnode.dev/mastering-sqlalchemy-relationships-exploring-the-backpopulates-parameter-and-different-relationship-types
"""
from sqlalchemy import Column, Date, Integer, VARCHAR, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship
from db_setup import Base
from utils import db_info

# get the postgres db schema name
schema = db_info.SCHEMA_NAME.value

class Customer(Base):
    __tablename__ = db_info.TABLE_CUSTOMER.value
    __table_args__ = {'schema' : schema}

    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(VARCHAR(20), unique=True, nullable=False)
    gender = Column(VARCHAR(10))  
    device_type = Column(VARCHAR(20))	
    login_type = Column(VARCHAR(20))

    orders = relationship("Order", back_populates="customer")

class Order(Base):
    __tablename__ = db_info.TABLE_ORDER.value
    __table_args__ = {'schema' : schema}
  

    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(VARCHAR(20), ForeignKey(f'{schema}.customer.customer_id'), nullable=False)
    order_date = Column(Date)
    order_priority = Column(VARCHAR(10))
    payment_method = Column(VARCHAR(20)) 

    customer = relationship("Customer", back_populates="orders")
    order_items = relationship("OrderItem", back_populates="orders")

class Product(Base):
    __tablename__ = db_info.TABLE_PRODUCT.value
    __table_args__ = {'schema' : schema}

    id = Column(Integer, primary_key=True, autoincrement=True)
    product_category = Column(VARCHAR(50)) 
    product_name = Column(VARCHAR(100)) 

    order_items = relationship("OrderItem", back_populates="product")

class OrderItem(Base):
    __tablename__ = db_info.TABLE_ORDER_ITEMS.value
    __table_args__ = {'schema' : schema}

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey(f'{schema}.order.id'), nullable=False)	
    product_id = Column(Integer, ForeignKey(f'{schema}.product.id'), nullable=False)
    quantity = Column(Integer)
    discount = Column(DECIMAL(5, 2))
    sales = Column(DECIMAL(10, 2))
    profit = Column(DECIMAL(10, 2))
    shipping_cost = Column(DECIMAL(10, 2))

    orders = relationship("Order", back_populates="order_items")
    product = relationship("Product", back_populates="order_items")  