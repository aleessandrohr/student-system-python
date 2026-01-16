from app.cli.utils import TERMINAL_WIDTH, exibir_aluno, limpar_tela, pausar
from app.models import Aluno


# Busca aluno por matrícula
def buscar_por_matricula(db):
    limpar_tela()
    print("=" * TERMINAL_WIDTH)
    print("BUSCAR ALUNO POR MATRÍCULA".center(TERMINAL_WIDTH))
    print("=" * TERMINAL_WIDTH)
    print()

    try:
        matricula = input("Digite a matrícula: ").strip()
        aluno = db.query(Aluno).filter(Aluno.matricula == matricula).first()

        if not aluno:
            print("\n❌ Aluno não encontrado!")
        else:
            exibir_aluno(aluno)

    except Exception as e:
        db.rollback()
        print(f"\n❌ Erro ao buscar aluno: {e}")

    pausar()
