from datetime import datetime

from app.cli.utils import TERMINAL_WIDTH, limpar_tela, pausar
from app.models import Aluno


def cadastrar_aluno(db):
    """Cadastra um novo aluno"""
    limpar_tela()
    print("=" * TERMINAL_WIDTH)
    print("    CADASTRAR NOVO ALUNO".center(TERMINAL_WIDTH))
    print("=" * TERMINAL_WIDTH)
    print()

    try:
        matricula = input("Matrícula: ").strip()
        if db.query(Aluno).filter(Aluno.matricula == matricula).first():
            print("\n❌ Erro: Matrícula já cadastrada!")
            pausar()
            return

        nome = input("Nome completo: ").strip()
        email = input("Email: ").strip()

        if db.query(Aluno).filter(Aluno.email == email).first():
            print("\n❌ Erro: Email já cadastrado!")
            pausar()
            return

        cpf = input("CPF (apenas números ou com formatação): ").strip()

        if db.query(Aluno).filter(Aluno.cpf == cpf).first():
            print("\n❌ Erro: CPF já cadastrado!")
            pausar()
            return

        data_nasc = input("Data de nascimento (DD/MM/AAAA): ").strip()
        data_nascimento = datetime.strptime(data_nasc, "%d/%m/%Y").date()

        curso = input("Curso: ").strip()
        periodo = int(input("Período (1-12): "))

        if periodo < 1 or periodo > 12:
            print("\n❌ Erro: Período deve ser entre 1 e 12!")
            pausar()
            return

        media_geral = float(
            input("Média geral (0.0-10.0) [Enter para 0.0]: ").strip() or "0.0"
        )

        if media_geral < 0 or media_geral > 10:
            print("\n❌ Erro: Média deve ser entre 0.0 e 10.0!")
            pausar()
            return

        # Criar aluno
        novo_aluno = Aluno(
            matricula=matricula,
            nome=nome,
            email=email,
            cpf=cpf,
            data_nascimento=data_nascimento,
            curso=curso,
            periodo=periodo,
            media_geral=media_geral,
            ativo=1,
        )

        db.add(novo_aluno)
        db.commit()

        print("\n✅ Aluno cadastrado com sucesso!")
        print(f"ID: {novo_aluno.id}")

    except ValueError as e:
        print(f"\n❌ Erro: Dados inválidos! {e}")
    except Exception as e:
        print(f"\n❌ Erro ao cadastrar aluno: {e}")
        db.rollback()

    pausar()
