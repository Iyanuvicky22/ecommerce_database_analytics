"""
Author: Ajeyomi Adeodyin Samuel
Email: adedoyinsamuel25@gmail.com
Date: 07-03-2025

https://fastapi.tiangolo.com/tutorial/body-fields/#import-field
"""
from pydantic import BaseModel, Field
from datetime import date


class Customers(BaseModel):
    id:int
    customer_id:int
    gender:str
    device_type:str
    login_type:str
        
class Orders:
    id:int
    customer_id:int
    order_date:date
    order_priority:str
    payment_method:str

class Products:
    id:int
    product_category:str
    product_name:str

class AnalyticsTopProducts:
    id:int
    product:str
    count:int
    pass

class AnalyticsRevenue():
    total_revenue:float = Field(gt=0)
    total_profit:float = Field(gt=0)

