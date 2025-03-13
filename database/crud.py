"""
Database Analysis for Business Insights

"""
from decimal import Decimal
from sqlalchemy.orm import Session
from sqlalchemy import text, Connection, CursorResult, func, desc, case
from database.db_setup import CustomersTable, Products, OrdersTable
from database.db_setup import OrderItemsTable


def query_db(query: str, conn: Connection) -> CursorResult:
    """
    Create a query to the database using session connection.
    Args:
        query (str): _description_
        conn (Connection): _description_

    Returns:
        CursorResult: Returns database rows via the .Row class,
            which provides additional API features and behaviors on
            top of the raw data returned by the DBAPI.
            Through the use of filters such as the .Result.scalars method,
            other kinds of objects may also be returned.
    """
    sql = text(query)
    results = conn.execute(sql)
    return results


def to_float(value) -> float:
    """
    Converts decimal values to float type.

    Args:
        value (Decimal): Database Decimal datatype

    Returns:
        float: float data type.
    """
    return float(value) if isinstance(value, Decimal) else value


# Customer Insights
def customer_insights(session: Session):
    """
    Customer table insights.
    Args:
        session (Session): Persistence operation manager in ORM

    Returns:
        dict : Customer table insights.
    """
    total_customers = session.query(CustomersTable).count()
    customer_web_device = session.query(CustomersTable).filter(
        CustomersTable.device_type.ilike('Web')).count()
    customer_mobile_device = session.query(CustomersTable).filter(
        CustomersTable.device_type.ilike('Mobile')).count()
    customer_login_member = session.query(CustomersTable).filter(
        CustomersTable.login_type.ilike('Member')).count()
    customer_login_guest = session.query(CustomersTable).filter(
        CustomersTable.login_type.ilike('Guest')).count()
    percentage_member = customer_login_member / total_customers
    percentage_guest = customer_login_guest / total_customers
    return {"total_customers": total_customers,
            "web_customer": customer_web_device,
            "mobile_customer": customer_mobile_device,
            "percentage_member": percentage_member,
            "percentage_guest": percentage_guest}


def top_product_by_sales(session: Session):
    """

    Args:
        session (Session): _description_

    Returns:
        _type_: _description_
    """
    top_5_product_by_sales = (session.query(
        Products.product_name,
        func.sum(OrderItemsTable.sales).label("total_sales")
    ).join(Products, OrderItemsTable.product_id == Products.id)
                              .group_by(Products.id, Products.product_name)
                              .order_by(desc('total_sales'))
                              .limit(5))

    summary = [{column: to_float(value) for column,
                value in row._mapping.items()}
               for row in top_5_product_by_sales.all()]
    return summary


def top_product_by_profit(session: Session):
    """

    Args:
        session (Session): _description_

    Returns:
        _type_: _description_
    """
    top_5_product_by_profit = (session.query(
        Products.product_name,
        func.sum(OrderItemsTable.profit).label("total_profit")
    ).join(Products, OrderItemsTable.product_id == Products.id)
                               .group_by(Products.id, Products.product_name)
                               .order_by(desc('total_profit'))
                               .limit(5))

    summary = [{column: to_float(value) for column,
                value in row._mapping.items()}
               for row in top_5_product_by_profit.all()]
    return summary


def top_product_categories_by_revenue(session: Session):
    """

    Args:
        session (Session): _description_

    Returns:
        _type_: _description_
    """
    subquery = (session.query(
        Products.product_category,
        func.sum(OrderItemsTable.sales).label("total_sales")
    ).join(Products, OrderItemsTable.product_id == Products.id)
                .group_by(Products.id, Products.product_category)
                .subquery()
                )
    top_3_product_category_by_revenue = (session.query(
        subquery.c.product_category, func.sum(subquery.c.total_sales).label(
            "total_category_sales")
    ).group_by(subquery.c.product_category).order_by(desc(
        "total_category_sales")).limit(3))
    summary = [{column: to_float(value) for column,
                value in row._mapping.items()}
               for row in top_3_product_category_by_revenue.all()]
    return summary


def product_performance(session: Session):
    """

    Args:
        session (Session): _description_

    Returns:
        _type_: _description_
    """
    t_p_b_p = top_product_by_profit(session)
    t_p_b_s = top_product_by_sales(session)
    t_p_c_b_r = top_product_categories_by_revenue(session)
    return {
        "top_product_by_profit": t_p_b_p,
        "top_product_by_sales": t_p_b_s,
        "top_product_categories_by_revenue": t_p_c_b_r
    }


def using_sql_alchemy(session: Session):
    """

    Args:
        session (Session): _description_
    """

    total = (session.query(func.sum(OrderItemsTable.sales).label("total_sales"),
                           func.sum(OrderItemsTable.profit)
                           .label("total_profit")))
    summary = [{column: to_float(value) for column,
                value in row._mapping.items()}
               for row in total.all()]
    print(summary)


def avg_order_size(session: Session):
    """
    MSsa
    Args:
        session (Session): _description_

    Returns:
        _type_: _description_
    """
    subquery = (session.query(OrderItemsTable.order_id, func.avg(
                OrderItemsTable.quantity).label("total_quantity"))
                .group_by(OrderItemsTable.order_id)).subquery()

    get_avg_order = session.query(
        func.round(func.avg(subquery.c.total_quantity), 2)
    ).scalar()
    return to_float(get_avg_order)


def total_profit_sales(session: Session):
    total = (session.query(func.sum(OrderItemsTable.sales).label("total_sales"),
                           func.sum(OrderItemsTable.profit)
                           .label("total_profit")))
    summary = [{column: to_float(value) for column,
                value in row._mapping.items()}
               for row in total.all()]
    return summary


def order_percentage(session: Session):
    """

    Args:
        session (Session): _description_

    Returns:
        _type_: _description_
    """
    percent = session.query(
        func.round(
            (func.sum(
                case(
                    (OrdersTable.order_priority.in_(['High', 'Critical']), 1),
                    else_=0
                )
            ) * 100.0) / func.count('*'),
            2
        ).label('order_percentage')
    ).select_from(OrdersTable).scalar()

    return to_float(percent)


def order_analysis(session: Session):
    """

    Args:
        session (Session): _description_

    Returns:
        _type_: _description_
    """
    o_p = order_percentage(session)
    t_p_s = total_profit_sales(session)
    a_o_s = avg_order_size(session)
    return {
        "order_percentage": o_p,
        "total_profit_revenue": t_p_s,
        "avg_order_size": a_o_s
    }


def discount_impact(session: Session):
    """

    Args:
        session (Session): _description_

    Returns:
        _type_: _description_
    """
    total = (
        session.query(
            OrderItemsTable.discount,
            func.sum(OrderItemsTable.sales).label('total_sales')
        )
        .group_by(OrderItemsTable.discount)
        .order_by(desc('total_sales'))
    )
    summary = [{column: to_float(value) for column,
                value in row._mapping.items()}
               for row in total.all()]
    return summary
