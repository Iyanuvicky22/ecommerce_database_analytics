"""
Author: Ajeyomi Adeodyin Samuel
Email: adedoyinsamuel25@gmail.com
Date: 07-03-2025


https://www.geeksforgeeks.org/introduction-to-psycopg2-module-in-python/
https://stackoverflow.com/questions/36359440/postgresql-insert-on-conflict-update-upsert-use-all-excluded-values
"""

# path to the data
DATA_PATH = r"C:\Users\Admin\Desktop\Data-engineering-internship\Task\Task 3\database-fundamentals\data\ecommerce_dataset.csv"

schema = "ecomerce"

# Insert customer data with ON CONFLICT handling
customer_query = f"""
                INSERT INTO {schema}.customer (customer_id, gender, device_type, login_type)
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (customer_id) 
                DO UPDATE SET 
                    gender = EXCLUDED.gender,
                    device_type = EXCLUDED.device_type,
                    login_type = EXCLUDED.login_type;   
"""

# Insert order data
order_query = f"""
                INSERT INTO {schema}.order(customer_id, order_date, order_priority, payment_method)
                VALUES (%s, %s, %s, %s)
"""

# Insert product data
product_query = f"""
                INSERT INTO {schema}.product (product_category, product_name)
                VALUES (%s, %s)
"""

# Insert order items data
order_items_query = f"""
                INSERT INTO {schema}.order_item(quantity, discount, sales, profit, shipping_cost)
                VALUES (%s, %s, %s, %s, %s)
"""
