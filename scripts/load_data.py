import pandas as pd
from database_fundamentals.database.db_setup import *


def load_data():
    # Session = connect_with_db()
    df = pd.read_csv("../data/ecommerce_dataset.csv", sep=',')

    df = df.drop_duplicates()
    print(df.describe())
    df["Quantity"] = df["Quantity"].fillna(0)
    df["Sales"] = df["Sales"].fillna(0)
    df["Discount"] = df["Discount"].fillna(0)
    df["Profit"] = df["Profit"].fillna(0)
    df["Shipping_Cost"] = df["Shipping_Cost"].fillna(0)
    with Session.begin() as session:
        # Inserting data into tables
        for _, row in df.iterrows():
            customer = session.query(Customer).filter_by(customer_id=str(row["Customer_Id"])).first()
            if not customer:
                customer = Customer(
                    id=uuid.uuid4(),
                    customer_id=str(row["Customer_Id"]),
                    gender=row["Gender"],
                    device_type=row["Device_Type"],
                    login_type=row["Customer_Login_type"],
                )
                session.add(customer)

            product = session.query(Products).filter_by(product_category=row["Product_Category"],
                                                        product_name=row["Product"]).first()
            if not product:
                product = Products(
                    id=uuid.uuid4(),
                    product_category=row["Product_Category"],
                    product_name=row["Product"]
                )
                session.add(product)

            orders = Orders(
                id=uuid.uuid4(),
                customer_id=customer.customer_id,
                order_date=row["Order_Date"],
                order_priority=row["Order_Priority"],
                payment_method=row["Payment_method"]
            )
            session.add(orders)

            order_item = OrderItems(
                id=uuid.uuid4(),
                order_id=orders.id,
                product_id=product.id,
                quantity=row["Quantity"],
                discount=row["Discount"],
                sales=row["Sales"],
                profit=row["Profit"],
                shipping_cost=row["Shipping_Cost"],
            )
            session.add(order_item)
        session.commit()


if __name__ == "__main__":
    load_data()
