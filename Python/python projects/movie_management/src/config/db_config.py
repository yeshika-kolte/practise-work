from mysql.connector import pooling, Error
from dotenv import load_dotenv
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent
ENV_PATH = BASE_DIR.parent / ".env"
load_dotenv(ENV_PATH)

try:
    pool = pooling.MySQLConnectionPool(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        pool_size=10,
    )
    print("Connection pool created successfully.")
except Error as e:
    print("Error creating connection pool:", e)
    pool = None
