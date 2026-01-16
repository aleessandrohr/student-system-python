import os

TERMINAL_WIDTH = 60


# Limpa a tela do terminal
def limpar_tela():
    os.system("clear" if os.name != "nt" else "cls")


# Pausa para o usuário ler a mensagem
def pausar():
    input("\nPressione ENTER para continuar...")


# Exibe os dados do aluno formatados
def exibir_aluno(aluno):
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


# Busca um aluno por ID ou Matrícula
def buscar_aluno(db):
    from app.models import Aluno

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
                return None

            return db.query(Aluno).filter(Aluno.id == aluno_id).first()

        # Busca aluno por matrícula
        case "2":
            matricula = input("Digite a matrícula do aluno: ").strip()

            if not matricula.isdigit():
                print("\n❌ Erro: Matrícula deve conter apenas números!")
                return None

            return db.query(Aluno).filter(Aluno.matricula == matricula).first()

        case _:
            print("\n❌ Opção inválida!")
            return None
