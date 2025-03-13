from sqlalchemy import create_engine
<<<<<<< HEAD
from sqlalchemy.orm import sessionmaker
from database_fundamentals.database.models import *
import logging
from sqlalchemy.exc import SQLAlchemyError
import psycopg2

def connect_with_db():
    try:
        database_url = 'postgresql://username:password@localhost/ecommerce_db'
        engine = create_engine(database_url)
        Session = sessionmaker(bind=engine)
        Base.metadata.create_all(engine)

        return Session, engine
    except SQLAlchemyError as e:
        logging.error(f"connection error: {str(e)}")
        return None, None
    except Exception as e:
        logging.error(f"error when connecting to database: {str(e)}")
        return None, None


if __name__ == "__main__":
    connect_with_db()
=======
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

>>>>>>> main
