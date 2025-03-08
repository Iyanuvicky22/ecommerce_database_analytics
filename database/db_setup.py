"""
Author: Ajeyomi Adeodyin Samuel
Email: adedoyinsamuel25@gmail.com
Date: 07-03-2025



"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os


# set the dabase URL
DATABASE_URL = os.environ.get("POSTGRESS_URL")

# create engine
engine = create_engine(DATABASE_URL)

# create session

SessionLocal = sessionmaker(
    autocomit=False, 
    autoflush=False,
    bind=engine,
    future=True
)


Base = declarative_base()

# db utils
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()