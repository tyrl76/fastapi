from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: int
    is_offer: bool = None

@app.get("/")
def read_root():
    return {"Hello": "world"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def save_item(item_id: int, item: Item):
    return {"item_id": item_id, "item_name": item.name, "item_price": item.price}