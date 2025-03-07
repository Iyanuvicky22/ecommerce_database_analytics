import uuid

from sqlalchemy import ForeignKey
from sqlalchemy import String, Date, Integer, DECIMAL,types,text
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class Base(DeclarativeBase):
    pass


class Customer(Base):
    __tablename__ = "customer"
    id: Mapped[uuid.UUID] = mapped_column(types.Uuid, primary_key=True, server_default=text("gen_random_uuid()"))
    customer_id: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    gender: Mapped[str] = mapped_column(String(10), nullable=False)
    device_type: Mapped[str] = mapped_column(String(20), nullable=False)
    login_type: Mapped[str] = mapped_column(String(20), nullable=False)

    # Relationship
    orders: Mapped["Orders"] = relationship("Orders", back_populates="customer")


class Orders(Base):
    __tablename__ = "orders"
    id: Mapped[uuid.UUID] = mapped_column(types.Uuid, primary_key=True, server_default=text("gen_random_uuid()"))
    customer_id: Mapped[str] = mapped_column(String(20), ForeignKey('customer.customer_id'), nullable=False)
    order_date: Mapped[Date] = mapped_column(Date, nullable=False)
    order_priority: Mapped[str] = mapped_column(String(10), nullable=False)
    payment_method: Mapped[str] = mapped_column(String(20), nullable=False)
    # Relationship
    customer: Mapped["Customer"] = relationship("Customer", back_populates="orders")
    order_item: Mapped["OrderItems"] = relationship("OrderItems", back_populates="orders")

class OrderItems(Base):
    __tablename__ = "order_items"
    id: Mapped[uuid.UUID] = mapped_column(types.Uuid, primary_key=True, server_default=text("gen_random_uuid()"))
    product_id: Mapped[uuid.UUID] = mapped_column(types.Uuid, ForeignKey('products.id'), nullable=False)
    order_id: Mapped[uuid.UUID] = mapped_column(types.Uuid, ForeignKey('orders.id'), nullable=False)
    quantity: Mapped[int] = mapped_column(Integer(), nullable=False, default=0)
    discount: Mapped[float] = mapped_column(DECIMAL(5, 2), nullable=False,default=0)
    sales: Mapped[float] = mapped_column(DECIMAL(10, 2), nullable=False,default=0)
    profit: Mapped[float] = mapped_column(DECIMAL(10, 2), nullable=False,default=0)
    shipping_cost: Mapped[float] = mapped_column(DECIMAL(10, 2), nullable=False,default=0)
    # Relationship
    orders: Mapped["Orders"] = relationship("Orders", back_populates="order_item")
    products: Mapped["Products"] = relationship("Products", back_populates="order_item")


class Products(Base):
    __tablename__ = "products"
    id: Mapped[uuid.UUID] = mapped_column(types.Uuid, primary_key=True,server_default=text("gen_random_uuid()"))
    product_category: Mapped[str] = mapped_column(String(50), nullable=False)
    product_name: Mapped[str] = mapped_column(String(100), nullable=False)

    # Relationship
    order_item: Mapped["OrderItems"] = relationship("OrderItems", back_populates="products")
