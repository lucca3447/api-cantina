from pydantic import BaseModel, Field

class FuncionarioCreate(BaseModel):
    nome: str= Field(min_length=2, max_length=100)
    cargo: str= Field(min_length=2, max_length=50)
    login: str= Field(min_length=2, max_length=50)
    senha: str= Field(min_length=8, max_length=100)
    


class FuncionarioUpdate(BaseModel):
    nome: str= Field(min_length=2, max_length=100)
    cargo: str= Field(min_length=2, max_length=50)
    login: str= Field(min_length=2, max_length=50)
    senha: str= Field(min_length=8, max_length=100)
    
    

class FuncionarioResponse(BaseModel):
    id_funcionario: int
    nome: str
    cargo: str
    login: str
    senha: str

    class Config:
        from_attributes = True