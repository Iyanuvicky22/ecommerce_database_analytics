from decimal import Decimal

from database_fundamentals.database.db_setup import *
from sqlalchemy import func
from sqlalchemy import text, Connection, CursorResult


def query_db(query: str, conn: Connection) -> CursorResult:
    sql = text(query)
    results = conn.execute(sql)
    return results


def to_float(value) -> float:
    return float(value) if isinstance(value, Decimal) else value


# Customer Insights
def customer_insights(conn: Connection):
    total_customers = query_db('SELECT COUNT(*) FROM customer', conn).scalar()
    customer_web_device = query_db("SELECT COUNT(*) FROM customer WHERE device_type ILIKE 'Web'", conn).scalar()
    customer_mobile_device = query_db("SELECT COUNT(*) FROM customer WHERE device_type ILIKE 'Mobile'", conn).scalar()
    customer_login_member = query_db("SELECT COUNT(*) FROM customer WHERE login_type ILIKE 'Member'", conn).scalar()
    customer_login_guest = query_db("SELECT COUNT(*) FROM customer WHERE login_type ILIKE 'Guest'", conn).scalar()
    percentage_member = int(customer_login_member) / int(total_customers)
    percentage_guest = int(customer_login_guest) / int(total_customers)
    return {"total_customers": total_customers,
            "web_customer": customer_web_device,
            "mobile_customer": customer_mobile_device,
            "percentage_member": percentage_member,
            "percentage_guest": percentage_guest}


def top_product_by_sales(conn: Connection):
    top_5_product_by_sales = query_db(
        "SELECT p.product_name, SUM(sales) AS total_sales FROM order_items oi JOIN products p ON oi.product_id = p.id "
        "GROUP BY p.id, p.product_name ORDER BY total_sales DESC LIMIT 5",
        conn)

    summary = [{column: to_float(value) for column, value in row._mapping.items()}
               for row in top_5_product_by_sales.all()]
    return summary


def top_product_by_profit(conn: Connection):
    top_5_product_by_sales = query_db(
        "SELECT p.product_name, SUM(profit) AS total_profit FROM order_items oi JOIN products p ON oi.product_id = "
        "p.id GROUP BY p.id, p.product_name ORDER BY total_profit DESC LIMIT 5",
        conn)

    summary = [{column: to_float(value) for column, value in row._mapping.items()}
               for row in top_5_product_by_sales.all()]
    return summary


def top_product_categories_by_revenue(conn: Connection):
    top_3_product_category_by_revenue = query_db(
        "SELECT product_category, SUM(total_sales) AS total_category_sales FROM (SELECT p.product_category, "
        "SUM(sales) AS total_sales FROM order_items oi JOIN products p ON oi.product_id = p.id GROUP BY p.id, "
        "p.product_category ORDER BY total_sales DESC )GROUP BY product_category ORDER BY total_category_sales DESC "
        "LIMIT 3",
        conn)

    summary = [{column: to_float(value) for column, value in row._mapping.items()}
               for row in top_3_product_category_by_revenue.all()]
    return summary


def product_performance(conn: Connection):
    t_p_b_p = top_product_by_profit(conn)
    t_p_b_s = top_product_by_sales(conn)
    t_p_c_b_r = top_product_categories_by_revenue(conn)
    return {
        "top_product_by_profit": t_p_b_p,
        "top_product_by_sales": t_p_b_s,
        "top_product_categories_by_revenue": t_p_c_b_r
    }


def avg_order_size(conn: Connection):
    get_avg_order = query_db(
        "SELECT ROUND(AVG(total_quantity),2) as avg_quantity FROM (SELECT order_id, SUM(quantity) AS total_quantity "
        "FROM order_items GROUP BY order_id)",
        conn).scalar()

    return to_float(get_avg_order)


def total_profit_revenue(conn: Connection):
    total = query_db(
        "SELECT SUM(sales) AS total_sales, SUM(profit) AS total_profit FROM order_items",
        conn)
    summary = [{column: to_float(value) for column, value in row._mapping.items()}
               for row in total.all()]
    return summary


def order_percentage(conn: Connection):
    percent = query_db(
        "SELECT ROUND((SUM(CASE WHEN order_priority = 'High' OR order_priority = 'Critical'  THEN 1 ELSE 0 END) * "
        "100.0) / COUNT(*),2) AS order_percentage FROM orders",
        conn).scalar()

    return to_float(percent)


def order_analysis(conn: Connection):
    o_p = order_percentage(conn)
    t_p_r = total_profit_revenue(conn)
    a_o_s = avg_order_size(conn)
    return {
        "order_percentage": o_p,
        "total_profit_revenue": t_p_r,
        "avg_order_size": a_o_s
    }


def discount_impact(conn: Connection):
    total = query_db(
        "SELECT discount, SUM(sales) AS total_sales FROM order_items GROUP BY discount ORDER BY total_sales DESC",
        conn)
    summary = [{column: to_float(value) for column, value in row._mapping.items()}
               for row in total.all()]
    return summary


if __name__ == "__main__":
    Session, engine = connect_with_db()
    # with Session.begin() as session:
    conn = engine.connect()
    # result = customer_insights(conn)
    # result = product_performance(conn)
    result = discount_impact(conn)
    print(result)
