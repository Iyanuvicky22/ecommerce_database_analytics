"""
Author: Ajeyomi Adeodyin Samuel
Email: adedoyinsamuel25@gmail.com
Date: 07-03-2025



"""

# set all depencies (module) part
import sys
sys.path.append('../')

from sqlalchemy.schema import CreateSchema
import model
from utils  import db_info
from db_setup import engine, get_db



def create_schema():
    # create schema
    with engine.connect() as connection:
        connection.execute(CreateSchema(db_info.SCHEMA_NAME.value,if_not_exists=True))
        connection.commit()

def create_table():
    create_schema()
    model.Base.metadata.create_all(bind=engine)
    get_db()


create_table()