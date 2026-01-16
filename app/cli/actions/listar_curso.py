from app.cli.utils import TERMINAL_WIDTH, limpar_tela, pausar
from app.models import Aluno


def listar_por_curso(db):
    """Lista alunos por curso"""
    limpar_tela()
    print("=" * TERMINAL_WIDTH)
    print("    LISTAR ALUNOS POR CURSO".center(TERMINAL_WIDTH))
    print("=" * TERMINAL_WIDTH)
    print()

    try:
        curso = input("Digite o nome do curso (ou parte dele): ").strip()
        alunos = db.query(Aluno).filter(Aluno.curso.ilike(f"%{curso}%")).all()

        if not alunos:
            print("\n📭 Nenhum aluno encontrado para este curso.")
        else:
            print(f"\nTotal de alunos: {len(alunos)}\n")
            for aluno in alunos:
                status = "✅ Ativo" if aluno.ativo == 1 else "❌ Inativo"
                print(f"\n{'─' * TERMINAL_WIDTH}")
                print(f"ID: {aluno.id} | Matrícula: {aluno.matricula}")
                print(f"Nome: {aluno.nome}")
                print(f"Curso: {aluno.curso} | Período: {aluno.periodo}")
                print(f"Média: {aluno.media_geral:.2f} | Status: {status}")

            print(f"\n{'─' * TERMINAL_WIDTH}")

    except Exception as e:
        print(f"\n❌ Erro ao listar alunos: {e}")

    pausar()
