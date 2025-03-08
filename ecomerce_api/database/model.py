"""
Author: Ajeyomi Adeodyin Samuel
Email: adedoyinsamuel25@gmail.com
Date: 07-03-2025



"""

from sqlalchemy import Column, Date, Integer, VARCHAR, DECIMAL
from db_setup import Base
from utils import db_info

class Customers(Base):
    __tablename__ = db_info.Customers.value

    id = Column(autoincrement=True, primary_key=True)
    customer_id = Column(VARCHAR(20), unique=True)
    gender = VARCHAR(10)
    device_type= Column(VARCHAR(20))	
    login_type = Column(VARCHAR(20))


class Order(Base):
    __tablename__ = db_info.Customers.value

    id = Column(autoincrement=True, primary_key=True)
    customer_id = Column(VARCHAR(20), unique=True)
    order_date = Column(Date)
    order_priority = Column(VARCHAR(10))
    payment_method = Column(VARCHAR(20)) 
   

class Product(Base):
    __tablename__ = db_info.Customers.value

    id = Column(autoincrement=True, primary_key=True)
    product_category = Column(VARCHAR(50)) 
    product_name = Column(VARCHAR(100)) 

class OrderITem(Base):
    __tablename__ = db_info.Customers.value

    id = Column(autoincrement=True, primary_key=True)
    order_id = Column(Integer, fk= Order(id))	
    product_id = Column(Integer, fk=PRoduct(id))
    quantity = Column(DECIMAL(5,2))
    sales = Column(DECIMAL(10,2))
    profit = Column(DECIMAL(10,2))
    shipping_cost = Column(DECIMAL(10,2))


