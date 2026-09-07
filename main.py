import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv()  # loads variables from the .env file into the environment

DATABASE_URL = os.getenv("DATABASE_URL")  # basically the Postgres connection string
engine = create_engine(
    DATABASE_URL
)  # setup the connection machinery, not connected yet
SessionLocal = sessionmaker(
    bind=engine
)  # factory that creates a new session per request
Base = (
    declarative_base()
)  # parent class models inherit from, so SQLAlchemy knows they're tables
