"""
Author: Ajeyomi Adeodyin Samuel
Email: adedoyinsamuel25@gmail.com
Date: 07-03-2025


https://www.geeksforgeeks.org/introduction-to-psycopg2-module-in-python/
"""


# Insert customer data with ON CONFLICT handling
customer_query = """
                INSERT INTO customer (customer_id, gender, device_type, customer_login_type)
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (customer_id) 
                DO UPDATE SET 
                    gender = EXCLUDED.gender,
                    device_type = EXCLUDED.device_type,
                    customer_login_type = EXCLUDED.customer_login_type;   
"""

# Insert order data
order_query = """
                INSERT INTO orders (customer_id, order_date, order_priority, payment_method)
                VALUES (%s, %s, %s, %s)
"""

# Insert product data
product_query = """
                INSERT INTO product (product_category, product)
                VALUES (%s, %s)
"""

# Insert order items data
order_items_query = """
                INSERT INTO order_items (order_id, quantity, discount, sales, profit, shipping_cost)
                VALUES (%s, %s, %s, %s, %s, %s)
"""
