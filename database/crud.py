from database_fundamentals.database.db_setup import *
from sqlalchemy import func

# Customer Insights
def customer_insights():
    Session = connect_with_db()
    with Session.begin() as session:
        users = session.query(func.count(Customer.id)).scalar()
        print(users)


if __name__ == "__main__":
    customer_insights()
