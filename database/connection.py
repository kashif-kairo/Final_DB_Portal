# import os
# from pathlib import Path

# from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# BASE_DIR = Path(__file___).resolve().parent.parent
# load_dotenv(BASE_DIR/".env")

DB_HOST = 'localhost'
DB_PORT = 3306
DB_USER = 'root'
DB_PASSWORD = ''
DB_NAME = 'db_admin_portal'
# print(DB_HOST)
# print(DB_PORT)
# print(DB_USER)
# print(__file__)


DATABASE_URL = (
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(
    DATABASE_URL,
    echo=False,
    pool_pre_ping=True
)