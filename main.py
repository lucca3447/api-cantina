from fastapi import FastAPI


from core.config import settings
from core.database import Base, engine

from models.categoria_model import Categoria
from routers.categoria_router import router as categoria_router


Base.metadata.create_all(bind=engine)

app = FastAPI(title="API para cantina", description="API para controle de cantina escolar", version="1.0")

app.include_router(categoria_router)

@app.get("/")
def home():
    return {
        "mensagem": "API da cantina funcionandokkkk"
    }