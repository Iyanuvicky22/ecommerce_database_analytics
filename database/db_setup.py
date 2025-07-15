"""
Setting up database and tables creation.

Name: Arowosegbe Victor Iyanuoluwa\n
Email: Iyanuvicky@gmail.com\n
GitHub: https://github.com/Iyanuvicky22/projects
"""
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from database.models import *
from utils.logger import logger


load_dotenv(dotenv_path=".env")
URL = os.getenv("DB_URL")


def connect_db():
    """
    Setting up database connection.
    """
    try:
        engine = create_engine(URL, echo=False)
        Session = sessionmaker(bind=engine)
        Base.metadata.create_all(engine)
        # session = Session()
        logger.info("Congratulations!!! Database successfully connected to.")
        # include logging
        return Session, engine
    except SQLAlchemyError as e:
        logger.error(f"Connection Error: {e}")


if __name__ == "__main__":
    connect_db()
