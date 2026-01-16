from app.cli.utils import limpar_tela, pausar
from app.models import Aluno


def atualizar_aluno(db):
    """Atualiza dados do aluno"""
    limpar_tela()
    print("=" * 60)
    print("    ATUALIZAR DADOS DO ALUNO".center(60))
    print("=" * 60)
    print()

    try:
        aluno_id = int(input("Digite o ID do aluno: "))
        aluno = db.query(Aluno).filter(Aluno.id == aluno_id).first()

        if not aluno:
            print("\n❌ Aluno não encontrado!")
            pausar()
            return

        print(f"\nAluno encontrado: {aluno.nome}")
        print("\nDeixe em branco para manter o valor atual\n")

        nome = input(f"Nome [{aluno.nome}]: ").strip()
        if nome:
            aluno.nome = nome

        email = input(f"Email [{aluno.email}]: ").strip()
        if email:
            aluno.email = email

        curso = input(f"Curso [{aluno.curso}]: ").strip()
        if curso:
            aluno.curso = curso

        periodo_str = input(f"Período [{aluno.periodo}]: ").strip()
        if periodo_str:
            periodo = int(periodo_str)
            if 1 <= periodo <= 12:
                aluno.periodo = periodo
            else:
                print("⚠️ Período inválido, mantendo valor atual")

        media_str = input(f"Média Geral [{aluno.media_geral}]: ").strip()
        if media_str:
            media = float(media_str)
            if 0 <= media <= 10:
                aluno.media_geral = media
            else:
                print("⚠️ Média inválida, mantendo valor atual")

        db.commit()
        print("\n✅ Aluno atualizado com sucesso!")

    except ValueError:
        print("\n❌ Erro: Dados inválidos!")
    except Exception as e:
        print(f"\n❌ Erro ao atualizar aluno: {e}")
        db.rollback()

    pausar()
