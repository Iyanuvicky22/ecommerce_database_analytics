


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

# Db utils
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()