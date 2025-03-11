import sys
import os
from sqlalchemy import engine_from_config, pool
from alembic import context
from dotenv import load_dotenv

from sql_agent_project.src.database import create_tables
from sql_agent_project.src.seed import seed_database

# Add the project root path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

# Load database configurations
load_dotenv()

# Import Base after setting sys.path correctly
from src.models import Base  # Ensure the model is correctly imported

# Alembic configuration
config = context.config

# Set database URL from environment variables
DATABASE_URL = os.getenv("DATABASE_URL")
DB_NAME = os.getenv("DB_NAME", "sql_agent_db")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")

if not DATABASE_URL:
    DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

config.set_main_option("sqlalchemy.url", DATABASE_URL)

def apply_migrations():
    """Apply database migrations and seed initial data."""
    create_tables()
    seed_database()
    print("Migrations successfully applied!")

# Execute when the application starts
apply_migrations()
