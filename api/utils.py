"""
Author: Ajeyomi Adeodyin Samuel
Email: adedoyinsamuel25@gmail.com
Date: 07-03-2025

"""

from sqlalchemy.orm import Session
from database.model import Customer, Order, Product , OrderItem


def get_customers(db:Session):
    """get all customers"""
    return db.query(
        Customer
    ).all()

def get_custmer_by_id(db:Session, customer_id:str):
    """get customer by customer_id"""
    return db.query(

    ).filter_by(customer_id).all()


def get_order(db:Session):
    """get all orders"""
    return db.query(
        Customer
    ).all()

def get_order_by_id(db:Session, order_id:str):
    """get order by order_id"""
    return db.query(

    ).filter_by(order_id).all()

def get_all_products(db:Session):
    """get all products"""
    return db.query(

    ).all()

def get_top_products(db:Session):
    """get all products"""
    return db.query(

    ).all()

def get_revenues(db:Session):
    """get all products"""
    return db.query(

    ).all()


