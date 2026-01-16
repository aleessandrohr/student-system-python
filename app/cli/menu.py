from app.cli.utils import limpar_tela


def exibir_menu():
    """Exibe o menu principal"""
    limpar_tela()
    print("=" * 60)
    print("    SISTEMA DE GERENCIAMENTO DE ALUNOS".center(60))
    print("=" * 60)
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
    print("\n" + "=" * 60)
