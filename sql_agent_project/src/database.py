from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.models import Base
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/sql_agent_db")

# Criar engine e sessão
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)

def create_tables():
    Base.metadata.create_all(engine)
    print("Tabelas criadas com sucesso!")


def get_db():
    """Cria uma sessão de banco de dados e garante que será fechada corretamente."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()    


    
