"""
Schemas Pydantic para validação de dados
"""
from pydantic import BaseModel, EmailStr, Field
from datetime import date
from typing import Optional


class AlunoBase(BaseModel):
    """Schema base para Aluno"""
    matricula: str = Field(..., min_length=5, max_length=20, description="Matrícula do aluno")
    nome: str = Field(..., min_length=3, max_length=100, description="Nome completo do aluno")
    email: EmailStr = Field(..., description="Email do aluno")
    cpf: str = Field(..., min_length=11, max_length=14, description="CPF do aluno")
    data_nascimento: date = Field(..., description="Data de nascimento")
    curso: str = Field(..., min_length=3, max_length=100, description="Curso do aluno")
    periodo: int = Field(..., ge=1, le=12, description="Período atual (1-12)")
    media_geral: Optional[float] = Field(default=0.0, ge=0.0, le=10.0, description="Média geral")
    ativo: Optional[int] = Field(default=1, ge=0, le=1, description="Status (1=ativo, 0=inativo)")


class AlunoCreate(AlunoBase):
    """Schema para criação de aluno"""
    pass


class AlunoUpdate(BaseModel):
    """Schema para atualização de aluno (campos opcionais)"""
    nome: Optional[str] = Field(None, min_length=3, max_length=100)
    email: Optional[EmailStr] = None
    curso: Optional[str] = Field(None, min_length=3, max_length=100)
    periodo: Optional[int] = Field(None, ge=1, le=12)
    media_geral: Optional[float] = Field(None, ge=0.0, le=10.0)
    ativo: Optional[int] = Field(None, ge=0, le=1)


class AlunoResponse(AlunoBase):
    """Schema para resposta de aluno"""
    id: int

    class Config:
        from_attributes = True
