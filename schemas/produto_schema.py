from pydantic import BaseModel, Field
from decimal import Decimal

class ProdutoCreate(BaseModel):
    nome: str = Field(..., min_length=2, max_length=100)
    preco: Decimal = Field(...,gt=0)
    id_categoria: int


class ProdutoUpdate(BaseModel):
    nome: str = Field(..., min_length=2, max_length=100)
    preco: Decimal = Field(..., gt=0)
    id_categoria: int

class ProdutoResponse(BaseModel):
    id_produto: int
    nome: str
    preco: Decimal
    id_categoria: int

    class Config:
        from_attributes = True