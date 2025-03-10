"""
Author: Ajeyomi Adeodyin Samuel
Email: adedoyinsamuel25@gmail.com
Date: 07-03-2025

"""

from fastapi import Depends, FastAPI, HTTPExecption, Path, APIRouter
from sqlalchemy.orm import Session

from schema import Customers,Orders,Products,AnalyticsRevenue,AnalyticsTopProducts
from database.db_setup import get_db
from utils import (get_custmer_by_id,get_customers,
                    get_custmer_by_id,get_all_products, get_order, 
                    get_order_by_id, get_revenues, get_top_products)


router = APIRouter



@router.get(


)

async def get_