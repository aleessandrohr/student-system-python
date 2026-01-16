from app.cli.utils import TERMINAL_WIDTH, exibir_aluno, limpar_tela, pausar
from app.models import Aluno


# Lista alunos por curso
def listar_por_curso(db):
    limpar_tela()
    print("=" * TERMINAL_WIDTH)
    print("LISTAR ALUNOS POR CURSO".center(TERMINAL_WIDTH))
    print("=" * TERMINAL_WIDTH)
    print()

    try:
        # Busca todos os alunos ordenados por curso
        alunos = db.query(Aluno).order_by(Aluno.curso).all()

        if not alunos:
            print("\n📭 Nenhum aluno cadastrado.")
        else:
            # Agrupa alunos por curso
            cursos = {}

            for aluno in alunos:
                if aluno.curso not in cursos:
                    cursos[aluno.curso] = []
                cursos[aluno.curso].append(aluno)

            # Exibe alunos de cada curso
            for curso, lista_alunos in cursos.items():
                print(f"\n🎓 {curso.upper()}: {len(lista_alunos)} alunos")
                for aluno in lista_alunos:
                    exibir_aluno(aluno)

    except Exception as e:
        db.rollback()
        print(f"\n❌ Erro ao listar alunos: {e}")

    pausar()
