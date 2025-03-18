<<<<<<< HEAD
"""
Setting up database and tables creation.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from database.models import *

URL = 'postgresql://postgres:apotiks@localhost:5432/ecommerce_db'


def connect_db():
    """
    Setting up database connection.
    """
    try:
        engine = create_engine(URL, echo=False)
        Session = sessionmaker(bind=engine)
        Base.metadata.create_all(engine)
        # session = Session()
        print('\n\nCongratulations!!! Database successfully connected to.\n\n')
        return Session, engine
    except SQLAlchemyError as e:
        print(f'Connection Error {e}')
        return None, None


if __name__ == '__main__':
    connect_db()
=======
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# PostgreSQL Database URL (update .env file with actual credentials)
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:Polola2003.@localhost/ecommerce_db")

# Create database engine
engine = create_engine(DATABASE_URL)

# Session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for ORM models
Base = declarative_base()

# Function to create tables
def init_db():
    from database import models  # Import models
    Base.metadata.create_all(bind=engine)

>>>>>>> 7395a4a75b210c7aee5889ae024bdee5af5b6fad
