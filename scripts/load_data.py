"""
Author: Ajeyomi Adeodyin Samuel
Email: adedoyinsamuel25@gmail.com
Date: 07-03-2025


https://www.geeksforgeeks.org/introduction-to-psycopg2-module-in-python/
"""
import sys
sys.path.append('../')

import pandas as pd
from config import (DATA_PATH, customer_query,
                    order_items_query, order_query, product_query)

from utils import conn

def read_data(data_path:str) -> pd.DataFrame:
    """ Read csv data to dataframe"""
    try:
        df = pd.read_csv(data_path)
        return df
    except ValueError as e:
        print(f"Error: {e}")

def transform_data(data: pd.DataFrame) -> pd.DataFrame:
    """Perform basic data transformation"""
    # Convert all column names to lowercase
    data.columns = [col.lower() for col in data.columns]
    
    # Drop duplicate rows
    df = data.drop_duplicates().copy()
    
    # Convert 'order_date' column to datetime format 
    df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
    
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
    with con.cursor() as cur:
        for _, row in data.iterrows():
            cur.execute(query, tuple(row.fillna(0)))
        
        con.commit()

def etl_pipeline():
    data = read_data(DATA_PATH)
    transformed_data = transform_data(data)
    with conn as con:
        load_data_db(create_customer_dataframe(transformed_data), customer_query, con)
        load_data_db(create_order_dataframe(transformed_data), order_query, con)
        load_data_db(create_product_dataframe(transformed_data), product_query, con)
        load_data_db(create_orderitems_dataframe(transformed_data), order_items_query, con)




etl_pipeline()
