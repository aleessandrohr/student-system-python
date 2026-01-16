from app.cli.utils import TERMINAL_WIDTH, limpar_tela, pausar
from app.models import Aluno


def buscar_por_matricula(db):
    """Busca aluno por matrícula"""
    limpar_tela()
    print("=" * TERMINAL_WIDTH)
    print("    BUSCAR ALUNO POR MATRÍCULA".center(TERMINAL_WIDTH))
    print("=" * TERMINAL_WIDTH)
    print()

    try:
        matricula = input("Digite a matrícula: ").strip()
        aluno = db.query(Aluno).filter(Aluno.matricula == matricula).first()

        if not aluno:
            print("\n❌ Aluno não encontrado!")
        else:
            status = "✅ Ativo" if aluno.ativo == 1 else "❌ Inativo"
            print(f"\n{'─' * TERMINAL_WIDTH}")
            print(f"ID: {aluno.id}")
            print(f"Matrícula: {aluno.matricula}")
            print(f"Nome: {aluno.nome}")
            print(f"Email: {aluno.email}")
            print(f"CPF: {aluno.cpf}")
            print(f"Data Nascimento: {aluno.data_nascimento.strftime('%d/%m/%Y')}")
            print(f"Curso: {aluno.curso}")
            print(f"Período: {aluno.periodo}")
            print(f"Média Geral: {aluno.media_geral:.2f}")
            print(f"Status: {status}")
            print(f"{'─' * TERMINAL_WIDTH}")

    except Exception as e:
        print(f"\n❌ Erro ao buscar aluno: {e}")

    pausar()
