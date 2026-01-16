from app.cli.utils import TERMINAL_WIDTH, limpar_tela, pausar
from app.models import Aluno


def desativar_aluno(db):
    """Desativa um aluno (exclusão lógica)"""
    limpar_tela()
    print("=" * TERMINAL_WIDTH)
    print("    DESATIVAR ALUNO".center(TERMINAL_WIDTH))
    print("=" * TERMINAL_WIDTH)
    print()

    try:
        aluno_id = int(input("Digite o ID do aluno: "))
        aluno = db.query(Aluno).filter(Aluno.id == aluno_id).first()

        if not aluno:
            print("\n❌ Aluno não encontrado!")
        else:
            print(f"\nAluno: {aluno.nome}")
            confirmar = input("Deseja desativar este aluno? (S/N): ").strip().upper()

            if confirmar == "S":
                aluno.ativo = 0
                db.commit()
                print("\n✅ Aluno desativado com sucesso!")
            else:
                print("\n❌ Operação cancelada.")

    except ValueError:
        print("\n❌ Erro: ID deve ser um número!")
    except Exception as e:
        print(f"\n❌ Erro ao desativar aluno: {e}")
        db.rollback()

    pausar()
