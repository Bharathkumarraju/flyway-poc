import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Use correct DB URL with actual database name
DATABASE_URL = os.getenv("DATABASE_URL", "mysql+pymysql://root:password12345@localhost:3306/sampleapp")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
