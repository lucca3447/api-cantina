from pydantic import BaseModel, Field
from decimal import Decimal
from datetime import datetime

class PedidoCreate(BaseModel):
    id_funcionario: int
    valor_total: Decimal= Field(..., ge=0)


class PedidoUpdate(BaseModel):
    id_funcionario: int
    valor_total: Decimal= Field(..., ge=0)
    

class PedidoResponse(BaseModel):
    id_nota_fiscal: int
    id_funcionario: int
    valor_total: Decimal 
    data_hora: datetime

    class Config:
        from_attributes = True