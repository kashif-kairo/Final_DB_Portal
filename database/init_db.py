from database.base import Base
from database.connection import engine

import database.models

Base.metadata.create_all(bind=engine)

print("Database tables created successfully.")