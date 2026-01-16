from app.cli.utils import limpar_tela, pausar
from app.models import Aluno


def buscar_por_id(db):
    """Busca aluno por ID"""
    limpar_tela()
    print("=" * 60)
    print("    BUSCAR ALUNO POR ID".center(60))
    print("=" * 60)
    print()

    try:
        aluno_id = int(input("Digite o ID: "))
        aluno = db.query(Aluno).filter(Aluno.id == aluno_id).first()

        if not aluno:
            print("\n❌ Aluno não encontrado!")
        else:
            status = "✅ Ativo" if aluno.ativo == 1 else "❌ Inativo"
            print(f"\n{'─' * 60}")
            print(f"ID: {aluno.id}")
            print(f"Matrícula: {aluno.matricula}")
            print(f"Nome: {aluno.nome}")
            print(f"Email: {aluno.email}")
            print(f"CPF: {aluno.cpf}")
            print(f"Data Nascimento: {aluno.data_nascimento.strftime('%d/%m/%Y')}")
            print(f"Curso: {aluno.curso}")
            print(f"Período: {aluno.periodo}")
            print(f"Média Geral: {aluno.media_geral:.2f}")
            print(f"Status: {status}")
            print(f"{'─' * 60}")

    except ValueError:
        print("\n❌ Erro: ID deve ser um número!")
    except Exception as e:
        print(f"\n❌ Erro ao buscar aluno: {e}")

    pausar()
