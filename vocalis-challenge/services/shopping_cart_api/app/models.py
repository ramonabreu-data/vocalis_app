from pydantic import BaseModel
from typing import List

class CartItem(BaseModel):
    product_name: str
    quantity: int

class ShoppingCart(BaseModel):
    user_id: str
    items: List[CartItem] = []