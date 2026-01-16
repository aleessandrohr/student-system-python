from app.cli.utils import limpar_tela, pausar
from app.models import Aluno


def listar_por_curso(db):
    """Lista alunos por curso"""
    limpar_tela()
    print("=" * 60)
    print("    LISTAR ALUNOS POR CURSO".center(60))
    print("=" * 60)
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
                print(f"\n{'─' * 60}")
                print(f"ID: {aluno.id} | Matrícula: {aluno.matricula}")
                print(f"Nome: {aluno.nome}")
                print(f"Curso: {aluno.curso} | Período: {aluno.periodo}")
                print(f"Média: {aluno.media_geral:.2f} | Status: {status}")

            print(f"\n{'─' * 60}")

    except Exception as e:
        print(f"\n❌ Erro ao listar alunos: {e}")

    pausar()
