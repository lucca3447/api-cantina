from fastapi import FastAPI


from core.config import settings
from core.database import Base, engine

from models.categoria_model import Categoria
from models.estoque_model import Estoque
from models.fornecedor_model import Fornecedor
from models.fornecedor_produto_model import FornecedorProduto
from models.funcionario_model import Funcionario
from models.item_pedido_model import ItemPedido
from models.pedido_model import Pedido
from models.produto_model import Produto
from routers.categoria_router import router as categoria_router


Base.metadata.create_all(bind=engine)

app = FastAPI(title="API para cantina", description="API para controle de cantina escolar", version="1.0")

app.include_router(categoria_router)

@app.get("/")
def home():
    return {
        "mensagem": "API da cantina funcionandokkkk"
    }
