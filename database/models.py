<<<<<<< HEAD
"""
Tables Creation
"""
from sqlalchemy import ForeignKey, Column, Integer
from sqlalchemy import String, Date, DECIMAL, Index
from sqlalchemy.orm import relationship, backref, declarative_base

Base = declarative_base()

class CustomersTable(Base):
    """
    Customer Table Definition Class

    Args:
        Base (Class): Table declarative class.
    """
    __tablename__ = 'Customers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(String(20), unique=True)
    gender = Column(String(10))
    device_type = Column(String(20))
    login_type = Column(String(20))
    customers = relationship('OrdersTable', backref='Customers')


class OrdersTable(Base):
    """
    Orders Table Definition Class

    Args:
        Base (Class): Table declarative class.
    """
    __tablename__ = 'Orders'

    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(String(20), ForeignKey('Customers.customer_id'))
    order_date = Column(Date)
    order_priority = Column(String(10))
    payment_method = Column(String(20))
    orders_ids = relationship('OrderItemsTable', backref=backref('Orders'))

    # Creating an index on 'customer_id' column
    __table_args__ = (
        Index('idx_order_customer', 'customer_id'),
        )


class Products(Base):
    """
    Products Table Definition Class

    Args:
        Base (Class): Table declarative class.
    """
    __tablename__ = 'Products'

    id = Column(Integer, primary_key=True, autoincrement=True)
    product_category = Column(String(50))
    product_name = Column(String(100))
    product_ids = relationship('OrderItemsTable', backref=backref('Products'))


class OrderItemsTable(Base):
    """
    Orders Items Table Definition Class

    Args:
        Base (Class): Table declarative class.
    """
    __tablename__ = 'Order_items'

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('Orders.id'))
    product_id = Column(Integer, ForeignKey('Products.id'))
    quantity = Column(Integer)
    discount = Column(DECIMAL(5, 2))
    sales = Column(DECIMAL(10, 2))
    profit = Column(DECIMAL(10, 2))
    shipping_cost = Column(DECIMAL(10, 2))

    # Creating an index on 'product_id' column
    __table_args__ = (
        Index("idx_product_sales", 'product_id'),
    )
=======
from sqlalchemy import Column, Integer, String, ForeignKey, Date, DECIMAL
from sqlalchemy.orm import relationship
from database.db_setup import Base

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(String(20), unique=True, nullable=False)
    gender = Column(String(10))
    device_type = Column(String(20))
    login_type = Column(String(20))

    orders = relationship("Order", back_populates="customer")


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(String(20), ForeignKey("customers.customer_id"), nullable=False)
    order_date = Column(Date, nullable=False)
    order_priority = Column(String(10))
    payment_method = Column(String(20))

    customer = relationship("Customer", back_populates="orders")
    order_items = relationship("OrderItem", back_populates="order")


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, autoincrement=True)
    product_category = Column(String(50), nullable=False)
    product_name = Column(String(100), nullable=False)

    order_items = relationship("OrderItem", back_populates="product")


class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    discount = Column(DECIMAL(5, 2), default=0)
    sales = Column(DECIMAL(10, 2), nullable=False)
    profit = Column(DECIMAL(10, 2), nullable=False)
    shipping_cost = Column(DECIMAL(10, 2), nullable=False)

    order = relationship("Order", back_populates="order_items")
    product = relationship("Product", back_populates="order_items")
>>>>>>> 7395a4a75b210c7aee5889ae024bdee5af5b6fad
