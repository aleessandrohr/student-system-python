from app.cli.utils import TERMINAL_WIDTH, exibir_aluno, limpar_tela, pausar
from app.models import Aluno


# Busca aluno por ID
def buscar_por_id(db):
    limpar_tela()
    print("=" * TERMINAL_WIDTH)
    print("BUSCAR ALUNO POR ID".center(TERMINAL_WIDTH))
    print("=" * TERMINAL_WIDTH)
    print()

    try:
        aluno_id = int(input("Digite o ID: "))
        aluno = db.query(Aluno).filter(Aluno.id == aluno_id).first()

        if not aluno:
            print("\n❌ Aluno não encontrado!")
        else:
            exibir_aluno(aluno)

    except ValueError:
        print("\n❌ Erro: ID deve ser um número!")
    except Exception as e:
        db.rollback()
        print(f"\n❌ Erro ao buscar aluno: {e}")

    pausar()
