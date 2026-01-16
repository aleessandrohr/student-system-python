from app.cli.utils import TERMINAL_WIDTH, limpar_tela


# Exibe o menu principal
def exibir_menu():
    limpar_tela()
    print("=" * TERMINAL_WIDTH)
    print("SISTEMA DE GERENCIAMENTO DE ALUNOS".center(TERMINAL_WIDTH))
    print("=" * TERMINAL_WIDTH)
    print("\n📚 MENU PRINCIPAL\n")
    print("1. Cadastrar novo aluno")
    print("2. Listar todos os alunos")
    print("3. Buscar aluno por matrícula")
    print("4. Buscar aluno por ID")
    print("5. Atualizar dados do aluno")
    print("6. Desativar aluno")
    print("7. Deletar aluno permanentemente")
    print("8. Listar alunos por curso")
    print("9. Estatísticas")
    print("0. Sair")
    print("\n" + "=" * TERMINAL_WIDTH)
