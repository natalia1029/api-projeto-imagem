from fastapi import FastAPI
from pydantic import BaseModel

# cria a nossa API
app = FastAPI()

# dado esperado na rota /saudacao
class Entrada(BaseModel):
    fonte: str

@app.post("/predict")
def saudacao(entrada: Entrada):
    msg = f"Olá, {entrada.fonte}!"
    return {"mensagem": msg}

# dado esperado na rota /dobro
class PedidoNumero(BaseModel):
    numero: float

@app.post("/dobro")
def dobro(pedido: PedidoNumero):
    return {"resultado": pedido.numero * 2}
