"""
Author: Ajeyomi Adeodyin Samuel
Email: adedoyinsamuel25@gmail.com
Date: 07-03-2025


https://docs.sqlalchemy.org/en/14/orm/declarative_tables.html
"""
from enum import Enum

class db_info(Enum):
    TABLE_CUSTOMER = 'customer'
    TABLE_ORDER = 'order'
    TABLE_PRODUCT = 'product'
    TABLE_ORDER_ITEMS = 'order_item'
    SCHEMA_NAME = 'ecomerce'