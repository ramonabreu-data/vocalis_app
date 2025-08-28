from fastapi import FastAPI, HTTPException
from . import crud
from .models import CartItem, ShoppingCart

app = FastAPI(title="Shopping Cart API")

@app.post("/cart/{user_id}/items", response_model=ShoppingCart)
def add_item(user_id: str, item: CartItem):
    return crud.add_item_to_cart(user_id, item)

@app.get("/cart/{user_id}", response_model=ShoppingCart)
def get_cart(user_id: str):
    return crud.get_or_create_cart(user_id)

@app.get("/health")
def read_root():
    return {"status": "ok", "service": "shopping-cart"}