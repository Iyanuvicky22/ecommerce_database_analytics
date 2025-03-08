from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_fundamentals.database.models import *
import logging
from sqlalchemy.exc import SQLAlchemyError


def connect_with_db():
    try:
        database_url = 'postgresql://mac:test@localhost/ecommerce_db'
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
