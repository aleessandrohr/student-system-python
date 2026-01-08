"""
Aplicação principal FastAPI para gerenciamento de alunos
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import init_db
from app.routes import alunos_router

# Criar instância do FastAPI
app = FastAPI(
    title="Sistema de Gerenciamento de Alunos",
    description="API REST para gerenciar cadastro de alunos com PostgreSQL",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, especifique as origens permitidas
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registrar rotas
app.include_router(alunos_router, prefix="/api/v1")


@app.on_event("startup")
async def startup_event():
    """
    Evento executado na inicialização da aplicação
    """
    print("🚀 Iniciando aplicação...")
    print("📊 Criando tabelas no banco de dados...")
    init_db()
    print("✅ Aplicação iniciada com sucesso!")


@app.get("/")
def root():
    """
    Endpoint raiz da API
    """
    return {
        "mensagem": "API de Gerenciamento de Alunos",
        "versao": "1.0.0",
        "documentacao": "/docs",
        "status": "online"
    }


@app.get("/health")
def health_check():
    """
    Endpoint para verificação de saúde da API
    """
    return {
        "status": "healthy",
        "database": "connected"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
