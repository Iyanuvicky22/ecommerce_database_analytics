"""
Author: Ajeyomi Adeodyin Samuel
Email: adedoyinsamuel25@gmail.com
Date: 07-03-2025


https://www.geeksforgeeks.org/introduction-to-psycopg2-module-in-python/
"""
import pandas as pd
import psycopg2
import sqlalchemy

def read_data(data_path:str) -> pd.DataFrame:
    """ Read csv data to dataframe"""
    try:
        df = pd.read_csv(data_path)
        return df
    except ValueError as e:
        print(f"Error: {e}")

def transform_data(data:pd.DataFrame)->pd.DataFrame:
    """Perfom Basic Data transformation"""
    # convert all columns to lower case
    df = data.columns = [col.lower()  for col in data.columns]
    # drop duplicates data
    df = df.drop_duplicates()
    #  conver the order data from object dtype to datetime
    df = df['order_date'] = pd.to_datetime(df['order_date'])
    return df

# data modelling 
def create_customer_dataframe(df):
    """Extract data for the customer table"""
    columns = ["customer_id", "gender", "device_type", "customer_login_type"]
    customer_df = df[columns]
    return customer_df

def create_order_dataframe(df):
    """Extract data for the order table"""
    columns = ["customer_id", "order_date", "order_priority", "payment_method"]
    order_df = df[columns]
    return order_df

def create_product_dataframe(df):
    """Extract data for the product table"""
    columns = ["product_category","product"]
    product_df = df[columns]
    return product_df

def create_orderitems_dataframe(df):
    """Extract data for the order items table"""
    columns = ["quantity","discount","sales","profit","shipping_cost"]
    order_items_df = df[columns]
    return order_items_df

def load_data_db(data: pd.DataFrame, query: str, con):
    """Load data into the database using an SQL query."""
    cur = con.cursor()
    
    for _, row in data.iterrows():
        cur.execute(query, tuple(row))  # Pass row data as a tuple

    con.commit()
    cur.close()
    con.close()


def main():
    read_data()
    transform_data()
    create_customer_dataframe
    create_order_dataframe
    create_orderitems_dataframe
    create_product_dataframe
    load_data_db()




