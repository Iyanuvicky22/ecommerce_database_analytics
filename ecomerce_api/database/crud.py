"""
Author: Ajeyomi Adeodyin Samuel
Email: adedoyinsamuel25@gmail.com
Date: 07-03-2025



"""

# set all depencies (module) part
import sys
sys.path.append('../')

from sqlalchemy.schema import CreateSchema
from database import model
from database.utils  import db_info
from database.db_setup import engine



def create_tables():
    # create schema
    with engine.connect() as connection:
        connection.execute(CreateSchema(db_info.SCHEMA_NAME.value,if_not_exists=True))
        connection.commit()

    model.Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
#    # call db 
    get_db()