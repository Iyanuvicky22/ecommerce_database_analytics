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
