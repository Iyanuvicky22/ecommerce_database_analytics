import pandas as pd
from sqlalchemy.orm import Session
from database.db_setup import SessionLocal, engine
from database.models import Customer, Order, Product, OrderItem

# Load CSV file
csv_path = "data/ecommerce_dataset.csv"
df = pd.read_csv(csv_path)

# Convert Date columns
df["Order_Date"] = pd.to_datetime(df["Order_Date"]).dt.date

# Initialize database session
session = SessionLocal()

try:
    # Insert Customers
    for _, row in df.iterrows():
        customer = session.query(Customer).filter_by(customer_id=row["Customer_id"]).first()
        if not customer:
            customer = Customer(
                customer_id=row["Customer_id"],
                gender=row["Gender"],
                device_type=row["Device_Type"],
                login_type=row["Customer_Login_Type"]
            )
            session.add(customer)

    session.commit()

    # Insert Products
    for _, row in df.iterrows():
        product = session.query(Product).filter_by(product_name=row["Product"]).first()
        if not product:
            product = Product(
                product_category=row["Product_Category"],
                product_name=row["Product"]
            )
            session.add(product)

    session.commit()

    # Insert Orders and Order Items
    for _, row in df.iterrows():
        order = Order(
            customer_id=row["Customer_id"],
            order_date=row["Order_Date"],
            order_priority=row["Order_Priority"],
            payment_method=row["Payment_method"]
        )
        session.add(order)
        session.commit()  # Commit to get order.id

        # Get product ID
        product = session.query(Product).filter_by(product_name=row["Product"]).first()

        # Insert OrderItem
        order_item = OrderItem(
            order_id=order.id,
            product_id=product.id,
            quantity=row["Quantity"],
            discount=row["Discount"],
            sales=row["Sales"],
            profit=row["Profit"],
            shipping_cost=row["Shipping_cost"]
        )
        session.add(order_item)

    session.commit()
    print("Data successfully loaded into PostgreSQL!")

except Exception as e:
    session.rollback()
    print(f"Error: {e}")
finally:
    session.close()
