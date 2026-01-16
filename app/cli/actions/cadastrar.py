from datetime import datetime

from app.cli.utils import TERMINAL_WIDTH, limpar_tela, pausar
from app.models import Aluno


# Cadastra um novo aluno
def cadastrar_aluno(db):
    limpar_tela()
    print("=" * TERMINAL_WIDTH)
    print("CADASTRAR NOVO ALUNO".center(TERMINAL_WIDTH))
    print("=" * TERMINAL_WIDTH)
    print()

    try:
        matricula = input("Matrícula: ").strip()

        # Verifica se a matrícula é válida
        if not matricula.isdigit():
            print("\n❌ Erro: Matrícula deve conter apenas números!")
            pausar()
            return

        # Verifica se a matrícula tem 11 dígitos
        if len(matricula) != 11:
            print("\n❌ Erro: Matrícula deve conter 11 dígitos!")
            pausar()
            return

        # Verifica se a matrícula já existe
        if db.query(Aluno).filter(Aluno.matricula == matricula).first():
            print("\n❌ Erro: Matrícula já cadastrada!")
            pausar()
            return

        nome = input("Nome completo: ").strip()
        email = input("Email: ").strip()

        # Verifica se o email já existe
        if db.query(Aluno).filter(Aluno.email == email).first():
            print("\n❌ Erro: Email já cadastrado!")
            pausar()
            return

        cpf = input("CPF (apenas números): ").strip()

        # Verifica se o CPF é válido
        if not cpf.isdigit():
            print("\n❌ Erro: CPF deve conter apenas números!")
            pausar()
            return

        # Verifica se o CPF tem 11 dígitos
        if len(cpf) != 11:
            print("\n❌ Erro: CPF deve conter 11 dígitos!")
            pausar()
            return

        # Verifica se o CPF já existe
        if db.query(Aluno).filter(Aluno.cpf == cpf).first():
            print("\n❌ Erro: CPF já cadastrado!")
            pausar()
            return

        data_nasc = input("Data de nascimento (DD/MM/AAAA): ").strip()
        # Formata a data de nascimento
        data_nascimento = datetime.strptime(data_nasc, "%d/%m/%Y").date()

        curso = input("Curso: ").strip()
        periodo = int(input("Período (1-12): "))

        # Verifica se o período é válido
        if periodo < 1 or periodo > 12:
            print("\n❌ Erro: Período deve ser entre 1 e 12!")
            pausar()
            return

        media_geral = float(
            input("Média geral (0.0-10.0) [Enter para 0.0]: ").strip() or "0.0"
        )

        # Verifica se a média geral é válida
        if media_geral < 0 or media_geral > 10:
            print("\n❌ Erro: Média deve ser entre 0.0 e 10.0!")
            pausar()
            return

        # Criar aluno
        novo_aluno = Aluno(
            nome=nome,
            email=email,
            cpf=cpf,
            data_nascimento=data_nascimento,
            matricula=matricula,
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
