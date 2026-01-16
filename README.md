# Sistema de Gerenciamento de Alunos (CLI)

Sistema de gerenciamento de cadastro de alunos via Interface de Linha de Comando (CLI) utilizando Python, SQLAlchemy e PostgreSQL.

## 📋 Funcionalidades

- ✅ Cadastro completo de alunos
- ✅ Listagem de alunos
- ✅ Listagem filtrada por curso
- ✅ Busca por ID ou Matrícula
- ✅ Atualização de dados cadastrais
- ✅ Desativação de alunos (Exclusão Lógica)
- ✅ Exclusão permanente de alunos
- ✅ Estatísticas do sistema
- ✅ Validação de dados (CPF, Matrícula, etc.)

## 🛠️ Tecnologias

- **Python 3.12+**
- **SQLAlchemy** - ORM para banco de dados
- **PostgreSQL** - Banco de dados relacional
- **Psycopg2** - Driver PostgreSQL

## 📦 Estrutura do Projeto

```
student-system-python/
├── app/
│   ├── cli/                # Lógica da Interface de Linha de Comando
│   │   ├── actions/        # Ações individuais (cadastrar, listar, etc.)
│   │   ├── menu.py         # Exibição do menu principal
│   │   ├── main.py         # Controlador principal da CLI
│   │   └── utils.py        # Utilitários (input, formatação, etc.)
│   ├── database/           # Configuração de conexão com banco
│   └── models/             # Modelos ORM (SQLAlchemy)
├── cli.py                  # Ponto de entrada da aplicação
├── requirements.txt        # Dependências do projeto
├── .env.example            # Exemplo de variáveis de ambiente
└── README.md               # Documentação
```

## 🚀 Instalação e Configuração

Siga os passos abaixo para configurar e rodar o projeto em seu ambiente local.

### 1. Pré-requisitos

- Python 3.12 ou superior instalado.
- PostgreSQL instalado e rodando.

### 2. Configurar o Ambiente Virtual (.venv)

É **altamente recomendado** usar um ambiente virtual para isolar as dependências.

```bash
# Crie o ambiente virtual
python3 -m venv .venv

# Ative o ambiente virtual (Linux/macOS)
source .venv/bin/activate

# Ative o ambiente virtual (Windows)
# .venv\Scripts\activate
```

### 3. Instalar Dependências

Com o ambiente virtual ativado, instale as bibliotecas necessárias:

```bash
pip install -r requirements.txt
```

### 4. Configurar Banco de Dados

1. Certifique-se de que o serviço do PostgreSQL está rodando.
2. Crie um banco de dados para o projeto:

```sql
CREATE DATABASE alunos_db;
```

3. Configure as variáveis de ambiente:
   - Copie o arquivo de exemplo:
     ```bash
     cp .env.example .env
     ```
   - Edite o arquivo `.env` com suas credenciais do PostgreSQL:
     ```env
     DATABASE_URL=postgresql://seu_usuario:sua_senha@localhost:5432/alunos_db
     ```

### 5. Executar a Aplicação

O banco de dados (tabelas) será criado automaticamente na primeira execução.

Para iniciar o sistema, execute o arquivo `cli.py`:

```bash
# Executando com python
python cli.py

# Ou executando diretamente (se tiver permissão de execução)
./cli.py
```

## 💻 Como Usar

Ao iniciar o programa, você verá o seguinte menu interativo:

```text
============================================================
             SISTEMA DE GERENCIAMENTO DE ALUNOS
============================================================

📚 MENU PRINCIPAL

1. Cadastrar novo aluno
2. Listar todos os alunos
3. Buscar aluno por matrícula
4. Buscar aluno por ID
5. Atualizar dados do aluno
6. Desativar aluno
7. Deletar aluno permanentemente
8. Listar alunos por curso
9. Estatísticas
0. Sair

============================================================
```

Basta digitar o número da opção desejada e pressionar ENTER.

## 📝 Notas

- **Exclusão Lógica (Desativar)**: A opção "Desativar aluno" apenas muda o status do aluno para inativo, mantendo o registro no banco para histórico.
- **Exclusão Permanente**: A opção "Deletar aluno permanentemente" remove o registro definitivamente do banco de dados.

## 📄 Licença

Este projeto é de código aberto para fins educacionais.
