from app.cli.utils import limpar_tela, pausar
from app.models import Aluno


def deletar_aluno(db):
    """Deleta um aluno permanentemente"""
    limpar_tela()
    print("=" * 60)
    print("    DELETAR ALUNO PERMANENTEMENTE".center(60))
    print("=" * 60)
    print()

    try:
        aluno_id = int(input("Digite o ID do aluno: "))
        aluno = db.query(Aluno).filter(Aluno.id == aluno_id).first()

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

    except ValueError:
        print("\n❌ Erro: ID deve ser um número!")
    except Exception as e:
        print(f"\n❌ Erro ao deletar aluno: {e}")
        db.rollback()

    pausar()
