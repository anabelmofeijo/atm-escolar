from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DB_DIR = os.path.join(BASE_DIR, 'db')  
os.makedirs(DB_DIR, exist_ok=True)  # Cria a pasta se não existir


DATABASE_URL = f"sqlite:///{os.path.join(DB_DIR, 'database.db')}"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

db = SessionLocal()

Base = declarative_base() 