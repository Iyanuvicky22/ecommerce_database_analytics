import os
import psycopg2
from dotenv import load_dotenv


# Load environment variables
load_dotenv()

URL = os.getenv("POSTGRESS_URL")

# Database connection function
def postgres_connect(url):
    try:
        conn = psycopg2.connect(url)
        print("Database connected successfully")
        return conn
    except Exception as e:
        print(f"Database Connection Failed: {e}")
        return None  # Explicitly returning None on failure

# Establish connection
conn = postgres_connect(URL)
