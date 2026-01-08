"""
Modelo de Aluno para o banco de dados
"""
from sqlalchemy import Column, Integer, String, Date, Float
from app.database import Base
from datetime import date


class Aluno(Base):
    __tablename__ = "alunos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    matricula = Column(String(20), unique=True, nullable=False, index=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    cpf = Column(String(14), unique=True, nullable=False)
    data_nascimento = Column(Date, nullable=False)
    curso = Column(String(100), nullable=False)
    periodo = Column(Integer, nullable=False)
    media_geral = Column(Float, default=0.0)
    ativo = Column(Integer, default=1)  # 1 = ativo, 0 = inativo

    def __repr__(self):
        return f"<Aluno(matricula='{self.matricula}', nome='{self.nome}', curso='{self.curso}')>"
