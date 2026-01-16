from app.cli.utils import TERMINAL_WIDTH, exibir_aluno, limpar_tela, pausar
from app.models import Aluno


# Lista todos os alunos
def listar_alunos(db):
    limpar_tela()
    print("=" * TERMINAL_WIDTH)
    print("LISTA DE ALUNOS".center(TERMINAL_WIDTH))
    print("=" * TERMINAL_WIDTH)
    print()

    try:
        alunos = db.query(Aluno).all()

        if not alunos:
            print("📭 Nenhum aluno cadastrado.")
        else:
            print(f"Total de alunos: {len(alunos)}\n")

            for aluno in alunos:
                exibir_aluno(aluno)

            print(f"\n{'─' * TERMINAL_WIDTH}")

    except Exception as e:
        print(f"\n❌ Erro ao listar alunos: {e}")

    pausar()
