from app.cli.utils import limpar_tela, pausar
from app.models import Aluno


def listar_alunos(db):
    """Lista todos os alunos"""
    limpar_tela()
    print("=" * 60)
    print("    LISTA DE ALUNOS".center(60))
    print("=" * 60)
    print()

    try:
        alunos = db.query(Aluno).all()

        if not alunos:
            print("📭 Nenhum aluno cadastrado.")
        else:
            print(f"Total de alunos: {len(alunos)}\n")
            for aluno in alunos:
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

            print(f"\n{'─' * 60}")

    except Exception as e:
        print(f"\n❌ Erro ao listar alunos: {e}")

    pausar()
