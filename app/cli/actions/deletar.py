from app.cli.utils import TERMINAL_WIDTH, buscar_aluno, limpar_tela, pausar
from app.models import Aluno


# Deleta um aluno permanentemente
def deletar_aluno(db):
    limpar_tela()
    print("=" * TERMINAL_WIDTH)
    print("DELETAR ALUNO PERMANENTEMENTE".center(TERMINAL_WIDTH))
    print("=" * TERMINAL_WIDTH)
    print()

    try:
        aluno = buscar_aluno(db)

        if not aluno:
            print("\n❌ Aluno não encontrado!")
        else:
            print(f"\nAluno: {aluno.nome}")
            print("⚠️  ATENÇÃO: Esta ação não pode ser desfeita!")
            confirmar = input("Digite 'DELETAR' para confirmar: ").strip()

            if confirmar == "DELETAR":
                db.delete(aluno)
                db.commit()
                print("\n✅ Aluno deletado permanentemente!")
            else:
                print("\n❌ Operação cancelada.")

    except Exception as e:
        print(f"\n❌ Erro ao deletar aluno: {e}")
        db.rollback()

    pausar()
