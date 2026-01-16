from datetime import date

from sqlalchemy import Column, Date, Float, Integer, String

from app.database import Base


# Modelo de Aluno para o banco de dados
class Aluno(Base):
    __tablename__ = "alunos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    cpf = Column(String(11), unique=True, nullable=False)
    data_nascimento = Column(Date, nullable=False)
    matricula = Column(String(11), unique=True, nullable=False, index=True)
    curso = Column(String(100), nullable=False)
    periodo = Column(Integer, nullable=False)
    media_geral = Column(Float, default=0.0)
    ativo = Column(Integer, default=1)

    #
    def __repr__(self):
        return f"<Aluno(nome='{self.nome}', matricula='{self.matricula}', curso='{self.curso}')>"
