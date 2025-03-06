import psycopg2
from sqlalchemy import create_engine
from models import Base


def connect_with_db():
    DATABASE_URL = 'postgresql://mac:test@localhost/ecommerce_db'
    engine = create_engine(DATABASE_URL, echo=True)
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    connect_with_db()
