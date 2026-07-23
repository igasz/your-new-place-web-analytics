from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# the same connection
DB_URL = "oracle+oracledb://yourplace:Password123@localhost:1521/?service_name=FREEPDB1"

engine = create_engine(DB_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# give our API access to the database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

Base = declarative_base()