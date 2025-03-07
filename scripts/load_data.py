import pandas as pd
from sqlalchemy.dialects.postgresql import insert

from database_fundamentals.database import models, db_setup


def load_data():
    Session = db_setup.connect_with_db()
    df = pd.read_csv("/database_fundamentals/data/ecommerce_dataset.csv", sep=',')
    df = df.drop_duplicates()
    print(df.describe())
    with Session.begin() as session:
        # Inserting data into table
        for _, row in df.iterrows():
            customer = session.query(models.Customer).filter_by(customer_id=row["Customer_Id"]).first()
            if not customer:
                customer = models.Customer(
                    customer_id=row["Customer_Id"],
                    gender=row["Gender"],
                    device_type=row["Device_Type"],
                    login_type=row["Customer_Login_type"],
                )
                session.add(customer)
                session.commit()

            product = session.query(models.Products).filter_by(product_category=row["Product_Category"],
                                                               product_name=row["Product"]).first()
            if not product:
                product = models.Products(
                    product_category=row["Product_Category"],
                    product_name=row["Product"]
                )
                session.add(product)
                session.commit()

            orders = models.Orders(
                customer_id=customer.customer_id,
                order_date=row["Order_Date"],
                order_priority=row["Order_Priority"],
                payment_method=row["Payment_method"]
            )
            session.add(orders)
            session.commit()

            order_item = models.OrderItems(
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


def insert_customer(session, customer_data):
    stmt = insert(models.Customer).values(customer_data)
    stmt = stmt.on_conflict_do_nothing(index_elements=['customer_id'])
    session.execute(stmt)
    session.commit()


if __name__ == "__main__":
    load_data()
