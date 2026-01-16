from app.cli.utils import TERMINAL_WIDTH, buscar_aluno, limpar_tela, pausar
from app.models import Aluno


# Desativa um aluno (exclusão lógica)
def desativar_aluno(db):
    limpar_tela()
    print("=" * TERMINAL_WIDTH)
    print("DESATIVAR ALUNO".center(TERMINAL_WIDTH))
    print("=" * TERMINAL_WIDTH)
    print()

    try:
        aluno = buscar_aluno(db)

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

    except Exception as e:
        print(f"\n❌ Erro ao desativar aluno: {e}")
        db.rollback()

    pausar()
