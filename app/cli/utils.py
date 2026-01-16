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
