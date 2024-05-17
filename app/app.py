from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import uvicorn
from initDb import StartDb
from service import lista_pedidos, pedido_id, delete_pedido, cria_pedido
import io

StartDb()

app = FastAPI()

class Pedido(BaseModel):
    usuario: str
    email: str
    descricao: str

@app.get("/pedidos")
def pedidos():
    try:
        return lista_pedidos()
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Erro ao listar pedidos")
    
@app.post("/novo")
def novo(task: Pedido):
    try:
        cria_pedido(task.usuario, task.email, task.descricao)
        return {"message": "Pedido registrado com sucesso"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Erro ao criar pedido")
     
@app.get("/pedidos/{id}")
def pedido(id: int):
    try:
        return pedido_id(id)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Erro ao buscar pedido")

@app.delete("/pedidos/{id}")
def Delete_Pedido(id: int):    
    try:
        delete_pedido(id)
        return {"message": "Pedido removido com sucesso"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Erro ao deletar pedido")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
