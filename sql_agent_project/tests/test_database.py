import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.database import get_db
import os
from dotenv import load_dotenv

load_dotenv()

# Database Configuration for Testing
TEST_DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(TEST_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture
def db_session():
    """Creates a new database session for a test."""
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()

def test_database_connection(db_session):
    """Test if the database connection is working."""
    result = db_session.execute("SELECT 1").fetchone()
    assert result is not None
    assert result[0] == 1

def test_table_existence(db_session):
    """Test if the required tables exist in the database."""
    tables = ["clients", "products", "transactions"]
    for table in tables:
        result = db_session.execute(f"SELECT to_regclass('public.{table}')").fetchone()
        assert result[0] is not None, f"Table {table} does not exist"
