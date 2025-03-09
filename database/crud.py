from decimal import Decimal
from sqlalchemy.orm import Session
from database_fundamentals.database.db_setup import *
from sqlalchemy import text, Connection, CursorResult, func, desc, Engine, case


def query_db(query: str, conn: Connection) -> CursorResult:
    sql = text(query)
    results = conn.execute(sql)
    return results


def to_float(value) -> float:
    return float(value) if isinstance(value, Decimal) else value


# Customer Insights
def customer_insights(session: Session):
    total_customers = session.query(Customer).count()
    customer_web_device = session.query(Customer).filter(Customer.device_type.ilike('Web')).count()
    customer_mobile_device = session.query(Customer).filter(Customer.device_type.ilike('Mobile')).count()
    customer_login_member = session.query(Customer).filter(Customer.login_type.ilike('Member')).count()
    customer_login_guest = session.query(Customer).filter(Customer.login_type.ilike('Guest')).count()
    percentage_member = customer_login_member / total_customers
    percentage_guest = customer_login_guest / total_customers
    return {"total_customers": total_customers,
            "web_customer": customer_web_device,
            "mobile_customer": customer_mobile_device,
            "percentage_member": percentage_member,
            "percentage_guest": percentage_guest}


def top_product_by_sales(session: Session):
    top_5_product_by_sales = (session.query(
        Products.product_name,
        func.sum(OrderItems.sales).label("total_sales")
    ).join(Products, OrderItems.product_id == Products.id)
                              .group_by(Products.id, Products.product_name)
                              .order_by(desc('total_sales'))
                              .limit(5))

    summary = [{column: to_float(value) for column, value in row._mapping.items()}
               for row in top_5_product_by_sales.all()]
    return summary


def top_product_by_profit(session: Session):
    top_5_product_by_profit = (session.query(
        Products.product_name,
        func.sum(OrderItems.profit).label("total_profit")
    ).join(Products, OrderItems.product_id == Products.id)
                               .group_by(Products.id, Products.product_name)
                               .order_by(desc('total_profit'))
                               .limit(5))

    summary = [{column: to_float(value) for column, value in row._mapping.items()}
               for row in top_5_product_by_profit.all()]
    return summary


def top_product_categories_by_revenue(session: Session):
    subquery = (session.query(
        Products.product_category,
        func.sum(OrderItems.sales).label("total_sales")
    ).join(Products, OrderItems.product_id == Products.id)
                .group_by(Products.id, Products.product_category)
                .subquery()
                )
    top_3_product_category_by_revenue = (session.query(
        subquery.c.product_category, func.sum(subquery.c.total_sales).label("total_category_sales")
    ).group_by(subquery.c.product_category).order_by(desc("total_category_sales")).limit(3))

    summary = [{column: to_float(value) for column, value in row._mapping.items()}
               for row in top_3_product_category_by_revenue.all()]
    return summary


def product_performance(session: Session):
    t_p_b_p = top_product_by_profit(session)
    t_p_b_s = top_product_by_sales(session)
    t_p_c_b_r = top_product_categories_by_revenue(session)
    return {
        "top_product_by_profit": t_p_b_p,
        "top_product_by_sales": t_p_b_s,
        "top_product_categories_by_revenue": t_p_c_b_r
    }


def using_sql_alchemy(session: Session):
    total = (session.query(func.sum(OrderItems.sales).label("total_sales"), func.sum(OrderItems.profit)
                           .label("total_profit")))
    summary = [{column: to_float(value) for column, value in row._mapping.items()}
               for row in total.all()]
    print(summary)


def avg_order_size(session: Session):
    subquery = (session.query(OrderItems.order_id, func.avg(OrderItems.quantity).label("total_quantity"))
                .group_by(OrderItems.order_id)).subquery()
    get_avg_order = session.query(
        func.round(func.avg(subquery.c.total_quantity), 2)
    ).scalar()

    return to_float(get_avg_order)


def total_profit_sales(session: Session):
    total = (session.query(func.sum(OrderItems.sales).label("total_sales"), func.sum(OrderItems.profit)
                           .label("total_profit")))
    summary = [{column: to_float(value) for column, value in row._mapping.items()}
               for row in total.all()]
    return summary


def order_percentage(session: Session):
    percent = session.query(
        func.round(
            (func.sum(
                case(
                    (Orders.order_priority.in_(['High', 'Critical']), 1),
                    else_=0
                )
            ) * 100.0) / func.count('*'),
            2
        ).label('order_percentage')
    ).select_from(Orders).scalar()

    return to_float(percent)


def order_analysis(session: Session):
    o_p = order_percentage(session)
    t_p_s = total_profit_sales(session)
    a_o_s = avg_order_size(session)
    return {
        "order_percentage": o_p,
        "total_profit_revenue": t_p_s,
        "avg_order_size": a_o_s
    }


def discount_impact(session: Session):
    total = (
        session.query(
            OrderItems.discount,
            func.sum(OrderItems.sales).label('total_sales')
        )
        .group_by(OrderItems.discount)
        .order_by(desc('total_sales'))
    )
    summary = [{column: to_float(value) for column, value in row._mapping.items()}
               for row in total.all()]
    return summary


