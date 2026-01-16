import sys

from sqlalchemy.orm import Session

from app.cli.actions.atualizar import atualizar_aluno
from app.cli.actions.buscar_id import buscar_por_id
from app.cli.actions.buscar_matricula import buscar_por_matricula
from app.cli.actions.cadastrar import cadastrar_aluno
from app.cli.actions.deletar import deletar_aluno
from app.cli.actions.desativar import desativar_aluno
from app.cli.actions.estatisticas import exibir_estatisticas
from app.cli.actions.listar import listar_alunos
from app.cli.actions.listar_curso import listar_por_curso
from app.cli.menu import exibir_menu
from app.cli.utils import limpar_tela, pausar
from app.database import SessionLocal, init_db


class SistemaAlunos:
    def __init__(self):
        self.db: Session = SessionLocal()
        init_db()

    def limpar_tela(self):
        limpar_tela()

    def pausar(self):
        pausar()

    def exibir_menu(self):
        exibir_menu()

    def cadastrar_aluno(self):
        cadastrar_aluno(self.db)

    def listar_alunos(self):
        listar_alunos(self.db)

    def buscar_por_matricula(self):
        buscar_por_matricula(self.db)

    def buscar_por_id(self):
        buscar_por_id(self.db)

    def atualizar_aluno(self):
        atualizar_aluno(self.db)

    def desativar_aluno(self):
        desativar_aluno(self.db)

    def deletar_aluno(self):
        deletar_aluno(self.db)

    def listar_por_curso(self):
        listar_por_curso(self.db)

    def exibir_estatisticas(self):
        exibir_estatisticas(self.db)

    def executar(self):
        """Executa o sistema"""
        while True:
            self.exibir_menu()

            try:
                opcao = input("\nEscolha uma opção: ").strip()

                if opcao == "1":
                    self.cadastrar_aluno()
                elif opcao == "2":
                    self.listar_alunos()
                elif opcao == "3":
                    self.buscar_por_matricula()
                elif opcao == "4":
                    self.buscar_por_id()
                elif opcao == "5":
                    self.atualizar_aluno()
                elif opcao == "6":
                    self.desativar_aluno()
                elif opcao == "7":
                    self.deletar_aluno()
                elif opcao == "8":
                    self.listar_por_curso()
                elif opcao == "9":
                    self.exibir_estatisticas()
                elif opcao == "0":
                    self.limpar_tela()
                    print("\n👋 Encerrando sistema...")
                    print("Obrigado por usar o Sistema de Gerenciamento de Alunos!\n")
                    self.db.close()
                    sys.exit(0)
                else:
                    print("\n❌ Opção inválida!")
                    self.pausar()

            except KeyboardInterrupt:
                self.limpar_tela()
                print("\n\n👋 Sistema encerrado pelo usuário.\n")
                self.db.close()
                sys.exit(0)
            except Exception as e:
                print(f"\n❌ Erro inesperado: {e}")
                self.pausar()


if __name__ == "__main__":
    sistema = SistemaAlunos()
    sistema.executar()
