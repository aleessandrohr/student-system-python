import os


def limpar_tela():
    """Limpa a tela do terminal"""
    os.system("clear" if os.name != "nt" else "cls")


def pausar():
    """Pausa para o usuário ler a mensagem"""
    input("\nPressione ENTER para continuar...")
