# Sistema de Gerenciamento de Alunos

API REST para gerenciamento de cadastro de alunos usando Python, FastAPI e PostgreSQL.

## 📋 Funcionalidades

- ✅ Cadastro completo de alunos
- ✅ Listagem de alunos com filtros (curso, status ativo)
- ✅ Busca por ID ou matrícula
- ✅ Atualização de dados
- ✅ Exclusão lógica e permanente
- ✅ Validação de dados com Pydantic
- ✅ Documentação automática (Swagger/ReDoc)

## 🛠️ Tecnologias

- **Python 3.8+**
- **FastAPI** - Framework web moderno e rápido
- **SQLAlchemy** - ORM para banco de dados
- **PostgreSQL** - Banco de dados relacional
- **Pydantic** - Validação de dados
- **Uvicorn** - Servidor ASGI

## 📦 Estrutura do Projeto

```
projeto/
├── app/
│   ├── __init__.py
│   ├── database/
│   │   ├── __init__.py
│   │   └── connection.py      # Configuração do banco
│   ├── models/
│   │   ├── __init__.py
│   │   └── aluno.py           # Modelo de dados
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── aluno.py           # Schemas de validação
│   └── routes/
│       ├── __init__.py
│       └── alunos.py          # Endpoints da API
├── main.py                     # Aplicação principal
├── requirements.txt            # Dependências
├── .env.example               # Exemplo de variáveis de ambiente
└── README.md                  # Este arquivo
```

## 🚀 Instalação e Configuração

### 1. Instalar dependências

```bash
pip install -r requirements.txt
```

### 2. Configurar banco de dados PostgreSQL

Crie um banco de dados PostgreSQL:

```sql
CREATE DATABASE alunos_db;
```

### 3. Configurar variáveis de ambiente

Copie o arquivo `.env.example` para `.env`:

```bash
cp .env.example .env
```

Edite o arquivo `.env` com suas credenciais do PostgreSQL:

```env
DATABASE_URL=postgresql://seu_usuario:sua_senha@localhost:5432/alunos_db
```

### 4. Executar a aplicação

#### Modo CLI (Interface de Terminal) - RECOMENDADO

```bash
python cli.py
```

#### Modo API (Servidor Web)

```bash
python main.py
```

Ou com uvicorn diretamente:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

A API estará disponível em: **http://localhost:8000**

## 📚 Documentação da API

Após iniciar a aplicação, acesse:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 💻 Interface CLI (Linha de Comando)

O sistema possui uma interface completa de terminal com menu interativo:

```bash
python cli.py
```

### Funcionalidades do CLI:

1. **Cadastrar novo aluno** - Adicionar aluno com todos os dados
2. **Listar todos os alunos** - Visualizar todos os alunos cadastrados
3. **Buscar aluno por matrícula** - Encontrar aluno específico
4. **Buscar aluno por ID** - Encontrar aluno por identificador
5. **Atualizar dados do aluno** - Modificar informações existentes
6. **Desativar aluno** - Exclusão lógica (mantém no banco)
7. **Deletar aluno permanentemente** - Exclusão física
8. **Listar alunos por curso** - Filtrar por curso específico
9. **Estatísticas** - Visualizar estatísticas do sistema

### Exemplo de uso do CLI:

```
====================================================================
               SISTEMA DE GERENCIAMENTO DE ALUNOS
====================================================================

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
```

## 🔌 Endpoints Disponíveis

### Alunos

| Método   | Endpoint                               | Descrição                         |
| -------- | -------------------------------------- | --------------------------------- |
| `POST`   | `/api/v1/alunos/`                      | Criar novo aluno                  |
| `GET`    | `/api/v1/alunos/`                      | Listar todos os alunos            |
| `GET`    | `/api/v1/alunos/{id}`                  | Obter aluno por ID                |
| `GET`    | `/api/v1/alunos/matricula/{matricula}` | Obter aluno por matrícula         |
| `PUT`    | `/api/v1/alunos/{id}`                  | Atualizar dados do aluno          |
| `DELETE` | `/api/v1/alunos/{id}`                  | Desativar aluno (exclusão lógica) |
| `DELETE` | `/api/v1/alunos/{id}/permanente`       | Deletar aluno permanentemente     |

### Exemplos de Uso

#### Criar um aluno

```bash
curl -X POST "http://localhost:8000/api/v1/alunos/" \
  -H "Content-Type: application/json" \
  -d '{
    "matricula": "2025001",
    "nome": "João Silva",
    "email": "joao.silva@email.com",
    "cpf": "123.456.789-00",
    "data_nascimento": "2000-05-15",
    "curso": "Ciência da Computação",
    "periodo": 3,
    "media_geral": 8.5
  }'
```

#### Listar alunos

```bash
curl "http://localhost:8000/api/v1/alunos/"
```

#### Listar alunos com filtros

```bash
# Por curso
curl "http://localhost:8000/api/v1/alunos/?curso=Computação"

# Apenas ativos
curl "http://localhost:8000/api/v1/alunos/?ativo=1"
```

#### Obter aluno por ID

```bash
curl "http://localhost:8000/api/v1/alunos/1"
```

#### Atualizar aluno

```bash
curl -X PUT "http://localhost:8000/api/v1/alunos/1" \
  -H "Content-Type: application/json" \
  -d '{
    "periodo": 4,
    "media_geral": 9.0
  }'
```

#### Desativar aluno

```bash
curl -X DELETE "http://localhost:8000/api/v1/alunos/1"
```

## 📊 Modelo de Dados - Aluno

| Campo             | Tipo        | Descrição                   | Restrições          |
| ----------------- | ----------- | --------------------------- | ------------------- |
| `id`              | Integer     | ID único                    | PK, Auto-incremento |
| `matricula`       | String(20)  | Matrícula do aluno          | Único, Not Null     |
| `nome`            | String(100) | Nome completo               | Not Null            |
| `email`           | String(100) | Email                       | Único, Not Null     |
| `cpf`             | String(14)  | CPF                         | Único, Not Null     |
| `data_nascimento` | Date        | Data de nascimento          | Not Null            |
| `curso`           | String(100) | Curso                       | Not Null            |
| `periodo`         | Integer     | Período atual (1-12)        | Not Null            |
| `media_geral`     | Float       | Média geral (0.0-10.0)      | Default: 0.0        |
| `ativo`           | Integer     | Status (1=ativo, 0=inativo) | Default: 1          |

## 🔧 Desenvolvimento

### Adicionar novas rotas

1. Crie um novo arquivo em `app/routes/`
2. Defina o router e endpoints
3. Registre o router em `main.py`

### Adicionar novos modelos

1. Crie um novo modelo em `app/models/`
2. Crie os schemas correspondentes em `app/schemas/`
3. Importe e use nas rotas

## 📝 Notas

- A exclusão padrão (`DELETE /alunos/{id}`) é lógica, apenas desativa o aluno
- Para exclusão permanente, use o endpoint `/alunos/{id}/permanente`
- Validações de email, CPF e matrícula únicos são aplicadas automaticamente
- O banco de dados é criado automaticamente na primeira execução

## 🤝 Contribuindo

Sinta-se à vontade para contribuir com melhorias!

## 📄 Licença

Este projeto é de código aberto para fins educacionais.
