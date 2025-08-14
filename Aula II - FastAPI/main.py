from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Modelo para itens
class Item(BaseModel):
    id: int
    nome: str
    preco: float

# Modelo para POST
class ItemInput(BaseModel):
    nome: str
    preco: float

class DeleteInput(BaseModel):
    id: int

# Modelo para resposta de POST
class ItemInputResponse(BaseModel):
    message: str
    dados: Item

# Lista de itens em memória
items = [Item(id=1, nome="Teclado", preco=199.90), Item(id=2, nome="Mouse", preco=89.90)]

# Rota GET
@app.get("/produtos", response_model=list[Item])
def listar_produtos():
    return [
       {"id": item.id, "nome": item.nome, "preco": item.preco} for item in items
    ]

# Rota POST
@app.post("/produtos", response_model=ItemInputResponse)
def criar_produto(item: ItemInput):
    novo_id = max(item.id for item in items) + 1
    novo_item = Item(id=novo_id, **item.model_dump())
    items.append(novo_item)
    response = ItemInputResponse(message="Produto criado com sucesso", dados=novo_item)
    return response.model_dump()


# Rota DELETE
@app.delete("/produtos", response_model=ItemInputResponse)
def deletar_produto(item: DeleteInput):
    item_deletado = next((i for i in items if i.id == item.id), None)
    if not item_deletado:
        return ItemInputResponse(message="Produto não encontrado", dados=None)
    items.remove(item_deletado)
    response = ItemInputResponse(message="Produto deletado com sucesso", dados=item_deletado)
    return response.model_dump()

# Rodar servidor:
# uvicorn main:app --reload