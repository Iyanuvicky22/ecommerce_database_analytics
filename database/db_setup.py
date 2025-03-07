from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_fundamentals.database.models import *

Session = None
def connect_with_db():
    database_url = 'postgresql://mac:test@localhost/ecommerce_db'
    engine = create_engine(database_url)
    global Session
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)

    return Session


if __name__ == "__main__":
    connect_with_db()
