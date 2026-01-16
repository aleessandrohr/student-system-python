import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

# URL de conexão com o PostgreSQL
DATABASE_URL = os.getenv(
    "DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/alunos_db"
)

# Criar engine do SQLAlchemy
engine = create_engine(DATABASE_URL, echo=False)

# Criar sessão
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para os modelos
Base = declarative_base()


def get_db():
    # Dependency para obter uma sessão do banco de dados
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


def init_db():
    # Inicializa o banco de dados criando todas as tabelas
    Base.metadata.create_all(bind=engine)
