"""


"""

import pandas as pd



def read_data(data_path) -> pd.DataFrame:
    """ Read csv data to dataframe"""
    try:
        df = pd.read_csv(data_path)
        return df
    except ValueError as e:
        print(f"Error: {e}")


# data modelling 
def create_customer_table():
    pass

def create_product_table():
    pass

def create_order_table():
    pass

def create_orderitems_Table():
    pass


def load_data_db(data:pd.DataFrame):
    pass