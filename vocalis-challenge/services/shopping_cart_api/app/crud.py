from .models import CartItem, ShoppingCart
from typing import Dict

# Simulação de um banco de dados em memória
db: Dict[str, ShoppingCart] = {}

def get_or_create_cart(user_id: str) -> ShoppingCart:
    if user_id not in db:
        db[user_id] = ShoppingCart(user_id=user_id)
    return db[user_id]

def add_item_to_cart(user_id: str, item: CartItem) -> ShoppingCart:
    cart = get_or_create_cart(user_id)
    # Lógica simples para adicionar ou atualizar a quantidade
    for existing_item in cart.items:
        if existing_item.product_name == item.product_name:
            existing_item.quantity += item.quantity
            return cart
    cart.items.append(item)
    return cart