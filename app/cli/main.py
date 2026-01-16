import sys

from sqlalchemy.orm import Session

from app.cli.actions import (
    atualizar_aluno,
    buscar_por_id,
    buscar_por_matricula,
    cadastrar_aluno,
    deletar_aluno,
    desativar_aluno,
    exibir_estatisticas,
    listar_alunos,
    listar_por_curso,
)
from app.cli.menu import exibir_menu
from app.cli.utils import limpar_tela, pausar
from app.database import SessionLocal, init_db


class SistemaAlunos:
    # Inicializa o sistema
    def __init__(self):
        self.db: Session = SessionLocal()
        init_db()

    # Executa o sistema
    def executar(self):
        while True:
            exibir_menu()

            try:
                opcao = input("\nEscolha uma opção: ").strip()

                match opcao:
                    case "1":
                        cadastrar_aluno(self.db)
                    case "2":
                        listar_alunos(self.db)
                    case "3":
                        buscar_por_matricula(self.db)
                    case "4":
                        buscar_por_id(self.db)
                    case "5":
                        atualizar_aluno(self.db)
                    case "6":
                        desativar_aluno(self.db)
                    case "7":
                        deletar_aluno(self.db)
                    case "8":
                        listar_por_curso(self.db)
                    case "9":
                        exibir_estatisticas(self.db)
                    case "0":
                        limpar_tela()
                        print("\n👋 Encerrando sistema...")
                        print(
                            "Obrigado por usar o Sistema de Gerenciamento de Alunos!\n"
                        )
                        self.db.close()
                        sys.exit(0)
                    case _:
                        print("\n❌ Opção inválida!")
                        pausar()

            except KeyboardInterrupt:
                limpar_tela()
                print("\n\n👋 Sistema encerrado pelo usuário.\n")
                self.db.close()
                sys.exit(0)

            except Exception as e:
                print(f"\n❌ Erro inesperado: {e}")
                pausar()
