from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config import settings
import os
from dotenv import load_dotenv

load_dotenv()
Database_url = os.getenv("Database_url")
engine = create_engine(settings.Database_url)
SessionLocal = sessionmaker(bind=engine)


Base=declarative_base()
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
