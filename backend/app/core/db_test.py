from sqlalchemy import create_engine, text  # <-- import text
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# Load .env variables
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Create engine and session
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Test connection
try:
    db = SessionLocal()
    db.execute(text("SELECT 1"))  # <-- wrap query in text()
    print("✅ Database connected successfully")
except Exception as e:
    print("❌ Database connection failed")
    print(e)
finally:
    db.close()
