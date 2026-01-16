import os

# Constante para o tamanho da tela
TERMINAL_WIDTH = 60


# Limpa a tela do terminal
def limpar_tela():
    os.system("clear" if os.name != "nt" else "cls")


# Pausa para o usuário ler a mensagem
def pausar():
    input("\nPressione ENTER para continuar...")
