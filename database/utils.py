"""
Author: Ajeyomi Adeodyin Samuel
Email: adedoyinsamuel25@gmail.com
Date: 07-03-2025


https://docs.sqlalchemy.org/en/14/orm/declarative_tables.html
"""
from enum import Enum

class db_info(Enum):
    TABLE_CUSTOMER = 'customers'
    TABLE_ORDER = 'orders'
    TABLE_PRODUCT = 'products'
    TABLE_ORDER_ITEMS = 'order_items'
    SCHEMA_NAME = 'ecomerce'