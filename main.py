from fastapi import FastAPI
from database_fundamentals.database.crud import *
from sqlalchemy import Engine

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to Damilola Adeniyi Database fundamental"}


@app.get("/customers/")
def get_all_customers(page: int = 1, size: int = 10):
    try:
        Session, engine = connect_with_db()
        if Session is None:
            raise "Failed to connect to database"
        offset = (page - 1) * size
        filter_customers = Session().query(Customer).offset(offset).limit(size)
        customer_list = [
            {"id": customer.id,
             "customer_id": customer.customer_id,
             "gender": customer.gender,
             "device_type": customer.device_type,
             "login_type": customer.login_type
             }
            for customer in filter_customers
        ]
        Session().close()
        return {
            "message": "Customers fetched",
            "success": True,
            "data": {
                "page": page,
                "size": size,
                "customers": customer_list,
            },
        }
    except Exception as e:
        logging.error(f"Unexpected error in get_all_customers: {str(e)}")
        return {
            "message": "An unexpected error occurred",
            "success": False,
            "data": None
        }


@app.get("/customers/{customer_id}")
def get_customers_by_customer_id(customer_id):
    try:
        Session, engine = connect_with_db()
        if Session is None:
            raise "Failed to connect to database"
        filter_customers = Session().query(Customer).filter_by(customer_id=customer_id).scalar()
        customer = {"id": filter_customers.id,
                    "customer_id": filter_customers.customer_id,
                    "gender": filter_customers.gender,
                    "device_type": filter_customers.device_type,
                    "login_type": filter_customers.login_type
                    }
        Session().close()
        return {
            "message": "Customer fetched",
            "success": True,
            "data": customer,
        }
    except Exception as e:
        logging.error(f"Unexpected error in get_all_products: {str(e)}")
        return {
            "message": "An unexpected error occurred",
            "success": False,
            "data": None
        }


@app.get("/orders/")
def get_all_orders(page: int = 1, size: int = 10):
    try:
        Session, engine = connect_with_db()
        if Session is None:
            raise "Failed to connect to database"
        offset = (page - 1) * size
        filter_orders = Session().query(Orders).offset(offset).limit(size)
        order_list = [
            {
                "id": order.id,
                "customer_id": order.customer_id,
                "order_date": order.order_date,
                "order_priority": order.order_priority,
                "payment_method": order.payment_method
            }
            for order in filter_orders
        ]
        Session().close()
        return {
            "message": "Orders fetched",
            "success": True,
            "data": {
                "page": page,
                "size": size,
                "customers": order_list,
            },
        }
    except Exception as e:
        logging.error(f"Unexpected error in get_all_products: {str(e)}")
        return {
            "message": "An unexpected error occurred",
            "success": False,
            "data": None
        }


@app.get("/orders/{order_id}")
def get_order_by_order_id(order_id):
    try:
        Session, engine = connect_with_db()
        if Session is None:
            raise "Failed to connect to database"
        filter_orders = Session().query(Orders).filter_by(id=order_id).scalar()
        order = {
            "id": filter_orders.id,
            "customer_id": filter_orders.customer_id,
            "order_date": filter_orders.order_date,
            "order_priority": filter_orders.order_priority,
            "payment_method": filter_orders.payment_method
        }
        Session().close()
        return {
            "message": "Order fetched",
            "success": True,
            "data": order,
        }
    except Exception as e:
        logging.error(f"Unexpected error in get_all_products: {str(e)}")
        return {
            "message": "An unexpected error occurred",
            "success": False,
            "data": None
        }


@app.get("/products/")
def get_all_products(page: int = 1, size: int = 10):
    try:
        Session, engine = connect_with_db()
        if Session is None:
            raise "Failed to connect to database"
        offset = (page - 1) * size
        filter_products = Session().query(Products).offset(offset).limit(size)
        product_list = [
            {
                "id": product.id,
                "product_category": product.product_category,
                "product_name": product.product_name
            }
            for product in filter_products
        ]
        Session().close()
        return {
            "message": "Products fetched",
            "success": True,
            "data": {
                "page": page,
                "size": size,
                "customers": product_list,
            },
        }
    except Exception as e:
        logging.error(f"Unexpected error in get_all_products: {str(e)}")
        return {
            "message": "An unexpected error occurred",
            "success": False,
            "data": None
        }


def get_session() -> Session:
    try:
        Session, engine = connect_with_db()
        if Session is None:
            raise "Failed to connect to database"
        return Session()
    except Exception as e:
        raise "Failed to connect to database"


@app.get("/analytics/top-products/")
def get_top_products():
    try:
        session = get_session()
        top_products = product_performance(session)
        session.close()

        return {
            "message": "Products fetched",
            "success": True,
            "data": top_products,
        }

    except Exception as e:
        logging.error(f"Unexpected error in get_top_products: {str(e)}")
        return {
            "message": "An unexpected error occurred",
            "success": False,
            "data": None
        }


@app.get("/analytics/revenue/")
def get_total_profit_revenue():
    try:
        session = get_session()
        total__revenue = order_analysis(session)
        session.close()
        return {
            "message": "Products fetched",
            "success": True,
            "data": total__revenue,
        }
    except Exception as e:
        logging.error(f"Unexpected error in get_total_profit_revenue: {str(e)}")
        return {
            "message": "An unexpected error occurred",
            "success": False,
            "data": None
        }


@app.get("/analytics/discount-impact/")
def get_discount_impact():
    try:
        session = get_session()
        impact = discount_impact(session)
        session.close()

        return {
            "message": "Discount impact data fetched successfully",
            "success": True,
            "data": impact,
        }
    except Exception as e:
        logging.error(f"Unexpected error in get_discount_impact: {str(e)}")
        return {
            "message": "An unexpected error occurred",
            "success": False,
            "data": None
        }
