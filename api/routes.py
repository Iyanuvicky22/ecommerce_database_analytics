from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.db_setup import SessionLocal
from database.models import Customer, Order, Product, OrderItem
from typing import List

router = APIRouter()

# Dependency: Get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Get all customers
@router.get("/customers/")
def get_customers(db: Session = Depends(get_db)):
    return db.query(Customer).all()

# Get customer details by ID
@router.get("/customers/{customer_id}")
def get_customer(customer_id: str, db: Session = Depends(get_db)):
    return db.query(Customer).filter(Customer.customer_id == customer_id).first()

# Get all orders
@router.get("/orders/")
def get_orders(db: Session = Depends(get_db)):
    return db.query(Order).all()

# Get order details by ID
@router.get("/orders/{order_id}")
def get_order(order_id: int, db: Session = Depends(get_db)):
    return db.query(Order).filter(Order.id == order_id).first()

# Get all products
@router.get("/products/")
def get_products(db: Session = Depends(get_db)):
    return db.query(Product).all()

# Get top-selling products (Analytics)
@router.get("/analytics/top-products/")
def get_top_products(db: Session = Depends(get_db)):
    query = db.execute("""
        SELECT p.product_name, SUM(oi.sales) AS total_sales
        FROM order_items oi
        JOIN products p ON oi.product_id = p.id
        GROUP BY p.product_name
        ORDER BY total_sales DESC
        LIMIT 5;
    """).fetchall()

    return [{"product_name": row[0], "total_sales": row[1]} for row in query]

# Get total revenue and profit (Analytics)
@router.get("/analytics/revenue/")
def get_revenue(db: Session = Depends(get_db)):
    revenue = db.query(
        db.query(OrderItem.sales).label("total_revenue"),
        db.query(OrderItem.profit).label("total_profit")
    ).first()
    
    return {"total_revenue": revenue.total_revenue, "total_profit": revenue.total_profit}
