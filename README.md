#  Sistema de Cantina

API RESTful para gerenciamento de cantina escolar, construída com **FastAPI + SQLAlchemy + MySQL**.
Segue a arquitetura em camadas **Router → Service → Repository**.

##  Estrutura de Pastas
```
app/
├── routers/          # Controladores (Endpoints)
├── services/         # Regras de Negócio
├── repositories/     # Consultas ao Banco de Dados (Queries)
├── models/           # Entidades do Banco (SQLAlchemy)
├── schemas/          # Validação de Dados (Pydantic / DTOs)
├── core/             # Configurações globais e Segurança (ou config/)
└── main.py           # Ponto de entrada da aplicação
```
##  Fluxo de uma Requisição

```
HTTP Request
    ↓
Router (recebe e valida o schema)
    ↓
Service (aplica regras de negócio)
    ↓
Repository (executa query no banco)
    ↓
HTTP Response
```

##  Como Rodar

```bash
# 1. Instale as dependências
pip install -r requirements.txt

# 2. Configure o banco
cp .env.example .env
# Edite o .env com suas credenciais MySQL

# 3. Suba o servidor
uvicorn main:app --reload
```





