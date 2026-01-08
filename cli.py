#!/usr/bin/env python3
"""
Interface de Linha de Comando (CLI) para o Sistema de Gerenciamento de Alunos
Execute: python cli.py
"""
import sys
from datetime import datetime
from sqlalchemy.orm import Session
from app.database import SessionLocal, init_db
from app.models import Aluno


class SistemaAlunos:
    def __init__(self):
        self.db: Session = SessionLocal()
        init_db()

    def limpar_tela(self):
        """Limpa a tela do terminal"""
        import os
        os.system('clear' if os.name != 'nt' else 'cls')

    def pausar(self):
        """Pausa para o usuário ler a mensagem"""
        input("\nPressione ENTER para continuar...")

    def exibir_menu(self):
        """Exibe o menu principal"""
        self.limpar_tela()
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

    def cadastrar_aluno(self):
        """Cadastra um novo aluno"""
        self.limpar_tela()
        print("=" * 60)
        print("    CADASTRAR NOVO ALUNO".center(60))
        print("=" * 60)
        print()

        try:
            matricula = input("Matrícula: ").strip()
            if self.db.query(Aluno).filter(Aluno.matricula == matricula).first():
                print("\n❌ Erro: Matrícula já cadastrada!")
                self.pausar()
                return

            nome = input("Nome completo: ").strip()
            email = input("Email: ").strip()

            if self.db.query(Aluno).filter(Aluno.email == email).first():
                print("\n❌ Erro: Email já cadastrado!")
                self.pausar()
                return

            cpf = input("CPF (apenas números ou com formatação): ").strip()

            if self.db.query(Aluno).filter(Aluno.cpf == cpf).first():
                print("\n❌ Erro: CPF já cadastrado!")
                self.pausar()
                return

            data_nasc = input("Data de nascimento (DD/MM/AAAA): ").strip()
            data_nascimento = datetime.strptime(data_nasc, "%d/%m/%Y").date()

            curso = input("Curso: ").strip()
            periodo = int(input("Período (1-12): "))

            if periodo < 1 or periodo > 12:
                print("\n❌ Erro: Período deve ser entre 1 e 12!")
                self.pausar()
                return

            media_geral = float(input("Média geral (0.0-10.0) [Enter para 0.0]: ").strip() or "0.0")

            if media_geral < 0 or media_geral > 10:
                print("\n❌ Erro: Média deve ser entre 0.0 e 10.0!")
                self.pausar()
                return

            # Criar aluno
            novo_aluno = Aluno(
                matricula=matricula,
                nome=nome,
                email=email,
                cpf=cpf,
                data_nascimento=data_nascimento,
                curso=curso,
                periodo=periodo,
                media_geral=media_geral,
                ativo=1
            )

            self.db.add(novo_aluno)
            self.db.commit()

            print("\n✅ Aluno cadastrado com sucesso!")
            print(f"ID: {novo_aluno.id}")

        except ValueError as e:
            print(f"\n❌ Erro: Dados inválidos! {e}")
        except Exception as e:
            print(f"\n❌ Erro ao cadastrar aluno: {e}")
            self.db.rollback()

        self.pausar()

    def listar_alunos(self):
        """Lista todos os alunos"""
        self.limpar_tela()
        print("=" * 60)
        print("    LISTA DE ALUNOS".center(60))
        print("=" * 60)
        print()

        try:
            alunos = self.db.query(Aluno).all()

            if not alunos:
                print("📭 Nenhum aluno cadastrado.")
            else:
                print(f"Total de alunos: {len(alunos)}\n")
                for aluno in alunos:
                    status = "✅ Ativo" if aluno.ativo == 1 else "❌ Inativo"
                    print(f"\n{'─' * 60}")
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

                print(f"\n{'─' * 60}")

        except Exception as e:
            print(f"\n❌ Erro ao listar alunos: {e}")

        self.pausar()

    def buscar_por_matricula(self):
        """Busca aluno por matrícula"""
        self.limpar_tela()
        print("=" * 60)
        print("    BUSCAR ALUNO POR MATRÍCULA".center(60))
        print("=" * 60)
        print()

        try:
            matricula = input("Digite a matrícula: ").strip()
            aluno = self.db.query(Aluno).filter(Aluno.matricula == matricula).first()

            if not aluno:
                print("\n❌ Aluno não encontrado!")
            else:
                status = "✅ Ativo" if aluno.ativo == 1 else "❌ Inativo"
                print(f"\n{'─' * 60}")
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
                print(f"{'─' * 60}")

        except Exception as e:
            print(f"\n❌ Erro ao buscar aluno: {e}")

        self.pausar()

    def buscar_por_id(self):
        """Busca aluno por ID"""
        self.limpar_tela()
        print("=" * 60)
        print("    BUSCAR ALUNO POR ID".center(60))
        print("=" * 60)
        print()

        try:
            aluno_id = int(input("Digite o ID: "))
            aluno = self.db.query(Aluno).filter(Aluno.id == aluno_id).first()

            if not aluno:
                print("\n❌ Aluno não encontrado!")
            else:
                status = "✅ Ativo" if aluno.ativo == 1 else "❌ Inativo"
                print(f"\n{'─' * 60}")
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
                print(f"{'─' * 60}")

        except ValueError:
            print("\n❌ Erro: ID deve ser um número!")
        except Exception as e:
            print(f"\n❌ Erro ao buscar aluno: {e}")

        self.pausar()

    def atualizar_aluno(self):
        """Atualiza dados do aluno"""
        self.limpar_tela()
        print("=" * 60)
        print("    ATUALIZAR DADOS DO ALUNO".center(60))
        print("=" * 60)
        print()

        try:
            aluno_id = int(input("Digite o ID do aluno: "))
            aluno = self.db.query(Aluno).filter(Aluno.id == aluno_id).first()

            if not aluno:
                print("\n❌ Aluno não encontrado!")
                self.pausar()
                return

            print(f"\nAluno encontrado: {aluno.nome}")
            print("\nDeixe em branco para manter o valor atual\n")

            nome = input(f"Nome [{aluno.nome}]: ").strip()
            if nome:
                aluno.nome = nome

            email = input(f"Email [{aluno.email}]: ").strip()
            if email:
                aluno.email = email

            curso = input(f"Curso [{aluno.curso}]: ").strip()
            if curso:
                aluno.curso = curso

            periodo_str = input(f"Período [{aluno.periodo}]: ").strip()
            if periodo_str:
                periodo = int(periodo_str)
                if 1 <= periodo <= 12:
                    aluno.periodo = periodo
                else:
                    print("⚠️ Período inválido, mantendo valor atual")

            media_str = input(f"Média Geral [{aluno.media_geral}]: ").strip()
            if media_str:
                media = float(media_str)
                if 0 <= media <= 10:
                    aluno.media_geral = media
                else:
                    print("⚠️ Média inválida, mantendo valor atual")

            self.db.commit()
            print("\n✅ Aluno atualizado com sucesso!")

        except ValueError:
            print("\n❌ Erro: Dados inválidos!")
        except Exception as e:
            print(f"\n❌ Erro ao atualizar aluno: {e}")
            self.db.rollback()

        self.pausar()

    def desativar_aluno(self):
        """Desativa um aluno (exclusão lógica)"""
        self.limpar_tela()
        print("=" * 60)
        print("    DESATIVAR ALUNO".center(60))
        print("=" * 60)
        print()

        try:
            aluno_id = int(input("Digite o ID do aluno: "))
            aluno = self.db.query(Aluno).filter(Aluno.id == aluno_id).first()

            if not aluno:
                print("\n❌ Aluno não encontrado!")
            else:
                print(f"\nAluno: {aluno.nome}")
                confirmar = input("Deseja desativar este aluno? (S/N): ").strip().upper()

                if confirmar == 'S':
                    aluno.ativo = 0
                    self.db.commit()
                    print("\n✅ Aluno desativado com sucesso!")
                else:
                    print("\n❌ Operação cancelada.")

        except ValueError:
            print("\n❌ Erro: ID deve ser um número!")
        except Exception as e:
            print(f"\n❌ Erro ao desativar aluno: {e}")
            self.db.rollback()

        self.pausar()

    def deletar_aluno(self):
        """Deleta um aluno permanentemente"""
        self.limpar_tela()
        print("=" * 60)
        print("    DELETAR ALUNO PERMANENTEMENTE".center(60))
        print("=" * 60)
        print()

        try:
            aluno_id = int(input("Digite o ID do aluno: "))
            aluno = self.db.query(Aluno).filter(Aluno.id == aluno_id).first()

            if not aluno:
                print("\n❌ Aluno não encontrado!")
            else:
                print(f"\nAluno: {aluno.nome}")
                print("⚠️  ATENÇÃO: Esta ação não pode ser desfeita!")
                confirmar = input("Digite 'DELETAR' para confirmar: ").strip()

                if confirmar == 'DELETAR':
                    self.db.delete(aluno)
                    self.db.commit()
                    print("\n✅ Aluno deletado permanentemente!")
                else:
                    print("\n❌ Operação cancelada.")

        except ValueError:
            print("\n❌ Erro: ID deve ser um número!")
        except Exception as e:
            print(f"\n❌ Erro ao deletar aluno: {e}")
            self.db.rollback()

        self.pausar()

    def listar_por_curso(self):
        """Lista alunos por curso"""
        self.limpar_tela()
        print("=" * 60)
        print("    LISTAR ALUNOS POR CURSO".center(60))
        print("=" * 60)
        print()

        try:
            curso = input("Digite o nome do curso (ou parte dele): ").strip()
            alunos = self.db.query(Aluno).filter(Aluno.curso.ilike(f"%{curso}%")).all()

            if not alunos:
                print("\n📭 Nenhum aluno encontrado para este curso.")
            else:
                print(f"\nTotal de alunos: {len(alunos)}\n")
                for aluno in alunos:
                    status = "✅ Ativo" if aluno.ativo == 1 else "❌ Inativo"
                    print(f"\n{'─' * 60}")
                    print(f"ID: {aluno.id} | Matrícula: {aluno.matricula}")
                    print(f"Nome: {aluno.nome}")
                    print(f"Curso: {aluno.curso} | Período: {aluno.periodo}")
                    print(f"Média: {aluno.media_geral:.2f} | Status: {status}")

                print(f"\n{'─' * 60}")

        except Exception as e:
            print(f"\n❌ Erro ao listar alunos: {e}")

        self.pausar()

    def exibir_estatisticas(self):
        """Exibe estatísticas do sistema"""
        self.limpar_tela()
        print("=" * 60)
        print("    ESTATÍSTICAS DO SISTEMA".center(60))
        print("=" * 60)
        print()

        try:
            total = self.db.query(Aluno).count()
            ativos = self.db.query(Aluno).filter(Aluno.ativo == 1).count()
            inativos = self.db.query(Aluno).filter(Aluno.ativo == 0).count()

            if total > 0:
                media_geral = self.db.query(Aluno).filter(Aluno.ativo == 1).all()
                media_sistema = sum([a.media_geral for a in media_geral]) / len(media_geral) if media_geral else 0
            else:
                media_sistema = 0

            # Cursos
            cursos = {}
            alunos = self.db.query(Aluno).all()
            for aluno in alunos:
                if aluno.curso in cursos:
                    cursos[aluno.curso] += 1
                else:
                    cursos[aluno.curso] = 1

            print(f"📊 Total de alunos cadastrados: {total}")
            print(f"✅ Alunos ativos: {ativos}")
            print(f"❌ Alunos inativos: {inativos}")
            print(f"📈 Média geral do sistema: {media_sistema:.2f}")

            if cursos:
                print(f"\n📚 Alunos por curso:")
                for curso, quantidade in sorted(cursos.items(), key=lambda x: x[1], reverse=True):
                    print(f"   • {curso}: {quantidade} aluno(s)")

        except Exception as e:
            print(f"\n❌ Erro ao calcular estatísticas: {e}")

        self.pausar()

    def executar(self):
        """Executa o sistema"""
        while True:
            self.exibir_menu()

            try:
                opcao = input("\nEscolha uma opção: ").strip()

                if opcao == '1':
                    self.cadastrar_aluno()
                elif opcao == '2':
                    self.listar_alunos()
                elif opcao == '3':
                    self.buscar_por_matricula()
                elif opcao == '4':
                    self.buscar_por_id()
                elif opcao == '5':
                    self.atualizar_aluno()
                elif opcao == '6':
                    self.desativar_aluno()
                elif opcao == '7':
                    self.deletar_aluno()
                elif opcao == '8':
                    self.listar_por_curso()
                elif opcao == '9':
                    self.exibir_estatisticas()
                elif opcao == '0':
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
