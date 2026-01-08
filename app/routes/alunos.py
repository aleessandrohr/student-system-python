"""
Rotas da API para gerenciamento de alunos
"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models import Aluno
from app.schemas import AlunoCreate, AlunoUpdate, AlunoResponse

router = APIRouter(
    prefix="/alunos",
    tags=["Alunos"]
)


@router.post("/", response_model=AlunoResponse, status_code=status.HTTP_201_CREATED)
def criar_aluno(aluno: AlunoCreate, db: Session = Depends(get_db)):
    """
    Criar um novo aluno
    """
    # Verificar se matrícula já existe
    db_aluno = db.query(Aluno).filter(Aluno.matricula == aluno.matricula).first()
    if db_aluno:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Matrícula já cadastrada"
        )

    # Verificar se email já existe
    db_aluno = db.query(Aluno).filter(Aluno.email == aluno.email).first()
    if db_aluno:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email já cadastrado"
        )

    # Verificar se CPF já existe
    db_aluno = db.query(Aluno).filter(Aluno.cpf == aluno.cpf).first()
    if db_aluno:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="CPF já cadastrado"
        )

    # Criar novo aluno
    novo_aluno = Aluno(**aluno.model_dump())
    db.add(novo_aluno)
    db.commit()
    db.refresh(novo_aluno)
    return novo_aluno


@router.get("/", response_model=List[AlunoResponse])
def listar_alunos(
    skip: int = 0,
    limit: int = 100,
    curso: str = None,
    ativo: int = None,
    db: Session = Depends(get_db)
):
    """
    Listar todos os alunos com filtros opcionais
    """
    query = db.query(Aluno)

    if curso:
        query = query.filter(Aluno.curso.ilike(f"%{curso}%"))

    if ativo is not None:
        query = query.filter(Aluno.ativo == ativo)

    alunos = query.offset(skip).limit(limit).all()
    return alunos


@router.get("/{aluno_id}", response_model=AlunoResponse)
def obter_aluno(aluno_id: int, db: Session = Depends(get_db)):
    """
    Obter um aluno específico pelo ID
    """
    aluno = db.query(Aluno).filter(Aluno.id == aluno_id).first()
    if not aluno:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Aluno não encontrado"
        )
    return aluno


@router.get("/matricula/{matricula}", response_model=AlunoResponse)
def obter_aluno_por_matricula(matricula: str, db: Session = Depends(get_db)):
    """
    Obter um aluno específico pela matrícula
    """
    aluno = db.query(Aluno).filter(Aluno.matricula == matricula).first()
    if not aluno:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Aluno não encontrado"
        )
    return aluno


@router.put("/{aluno_id}", response_model=AlunoResponse)
def atualizar_aluno(
    aluno_id: int,
    aluno_update: AlunoUpdate,
    db: Session = Depends(get_db)
):
    """
    Atualizar dados de um aluno
    """
    aluno = db.query(Aluno).filter(Aluno.id == aluno_id).first()
    if not aluno:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Aluno não encontrado"
        )

    # Atualizar apenas os campos fornecidos
    update_data = aluno_update.model_dump(exclude_unset=True)

    # Verificar se email já existe (se estiver sendo atualizado)
    if "email" in update_data and update_data["email"] != aluno.email:
        db_aluno = db.query(Aluno).filter(Aluno.email == update_data["email"]).first()
        if db_aluno:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email já cadastrado"
            )

    for field, value in update_data.items():
        setattr(aluno, field, value)

    db.commit()
    db.refresh(aluno)
    return aluno


@router.delete("/{aluno_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_aluno(aluno_id: int, db: Session = Depends(get_db)):
    """
    Deletar um aluno (exclusão lógica - apenas desativa)
    """
    aluno = db.query(Aluno).filter(Aluno.id == aluno_id).first()
    if not aluno:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Aluno não encontrado"
        )

    # Exclusão lógica
    aluno.ativo = 0
    db.commit()
    return None


@router.delete("/{aluno_id}/permanente", status_code=status.HTTP_204_NO_CONTENT)
def deletar_aluno_permanente(aluno_id: int, db: Session = Depends(get_db)):
    """
    Deletar um aluno permanentemente do banco de dados
    """
    aluno = db.query(Aluno).filter(Aluno.id == aluno_id).first()
    if not aluno:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Aluno não encontrado"
        )

    db.delete(aluno)
    db.commit()
    return None
