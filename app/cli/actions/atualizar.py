from app.cli.utils import TERMINAL_WIDTH, limpar_tela, pausar
from app.models import Aluno


# Atualiza dados do aluno
def atualizar_aluno(db):
    limpar_tela()
    print("=" * TERMINAL_WIDTH)
    print("ATUALIZAR DADOS DO ALUNO".center(TERMINAL_WIDTH))
    print("=" * TERMINAL_WIDTH)
    print()

    try:
        aluno = None

        print("Buscar aluno por:")
        print("1. ID")
        print("2. Matrícula")

        opcao = input("Opção: ").strip()
        match opcao:
            # Busca aluno por ID
            case "1":
                aluno_id = input("Digite o ID do aluno: ").strip()

                if not aluno_id.isdigit():
                    print("\n❌ Erro: ID deve conter apenas números!")
                    pausar()
                    return

                aluno = db.query(Aluno).filter(Aluno.id == aluno_id).first()

            # Busca aluno por matrícula
            case "2":
                matricula = input("Digite a matrícula do aluno: ").strip()

                if not matricula.isdigit():
                    print("\n❌ Erro: Matrícula deve conter apenas números!")
                    pausar()
                    return

                aluno = db.query(Aluno).filter(Aluno.matricula == matricula).first()

            case _:
                print("\n❌ Opção inválida!")
                pausar()

        if not aluno:
            print("\n❌ Aluno não encontrado!")
            pausar()
            return

        print(f"\nAluno encontrado: {aluno.nome}")
        print("\nDeixe em branco para manter o valor atual\n")

        # Atualiza campos de texto
        aluno.nome = input(f"Nome [{aluno.nome}]: ").strip() or aluno.nome
        aluno.email = input(f"Email [{aluno.email}]: ").strip() or aluno.email
        aluno.curso = input(f"Curso [{aluno.curso}]: ").strip() or aluno.curso

        # Atualiza campos numéricos
        try:
            periodo = int(
                input(f"Período [{aluno.periodo}]: ").strip() or aluno.periodo
            )
            if 1 <= periodo <= 12:
                aluno.periodo = periodo
            else:
                print("⚠️ Período inválido (deve ser 1-12), mantendo valor atual")
        except ValueError:
            print("⚠️ Valor inválido para período, mantendo valor atual")

        try:
            media = float(
                input(f"Média Geral [{aluno.media_geral}]: ").strip()
                or aluno.media_geral
            )
            if 0 <= media <= 10:
                aluno.media_geral = media
            else:
                print("⚠️ Média inválida (deve ser 0-10), mantendo valor atual")
        except ValueError:
            print("⚠️ Valor inválido para média, mantendo valor atual")

        db.commit()
        print("\n✅ Aluno atualizado com sucesso!")

    except Exception as e:
        print(f"\n❌ Erro ao atualizar aluno: {e}")
        db.rollback()

    pausar()
