from fastapi import FastAPI

app = FastAPI(title="API para cantina", description="API para controle de cantina escolar", version="1.0")

@app.get("/")
def home():
    return {
        "mensagem": "API da cantina funcionandokkkk"
    }