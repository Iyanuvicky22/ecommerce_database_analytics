from sqlalchemy import create_engine
from models import Base
from sqlalchemy.orm import sessionmaker


def connect_with_db():
    DATABASE_URL = 'postgresql://mac:test@localhost/ecommerce_db'
    engine = create_engine(DATABASE_URL, echo=True)
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)

    return Session


if __name__ == "__main__":
    connect_with_db()
