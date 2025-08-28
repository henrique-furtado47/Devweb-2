from fastapi import FastAPI, Query
from typing import Optional

app = FastAPI()

produtos = [
    {"id": 1, "nome": "Notebook", "preco": 3500},
    {"id": 2, "nome": "Mouse", "preco": 80},
    {"id": 3, "nome": "Teclado", "preco": 150},
    {"id": 4, "nome": "Monitor", "preco": 1200},
    {"id": 5, "nome": "Impressora", "preco": 300},
]

@app.get("/produtos/{id_produto}")
def get_produto(id_produto: int):
    for produto in produtos:
        if produto["id"] == id_produto:
            return produto
    return {"erro": "Produto não encontrado"}

@app.get("/produtos")
def listar_produtos(categoria: Optional[str] = None, min_preco: Optional[float] = Query(None, description="Preço mínimo"), max_preco: Optional[float] = Query(None, description="Preço máximo")):

    resultado = produtos
    if min_preco is not None:
        resultado = [p for p in resultado if p["preco"] >= min_preco]

    if max_preco is not None:
        resultado = [p for p in resultado if p["preco"] <= max_preco]

    return {"produtos": resultado}