import httpx
from langchain.tools import tool
from pydantic import BaseModel, Field

from src.core.config import settings

# Define o schema de entrada para a nossa ferramenta usando Pydantic.
# O LLM usará as descrições para entender o que cada campo significa.
class CartInput(BaseModel):
    product_name: str = Field(description="O nome do produto a ser adicionado ao carrinho.")
    quantity: int = Field(description="A quantidade do produto a ser adicionada.")

# O decorator @tool transforma a função em um objeto LangChain Tool.
@tool("add-item-to-cart", args_schema=CartInput)
async def add_item_to_cart(product_name: str, quantity: int) -> str:
    """Use esta ferramenta para adicionar itens ao carrinho de compras do usuário."""

    # O ID do usuário será fixo para este MVP
    user_id = "user123"
    url = f"{settings.SHOPPING_CART_API_URL}/cart/{user_id}/items"

    payload = {"product_name": product_name, "quantity": quantity}

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(url, json=payload)
            response.raise_for_status()  # Lança uma exceção para respostas de erro (4xx ou 5xx)

            # A resposta para o LLM deve ser em linguagem natural.
            return f"Sucesso! {quantity} unidade(s) de '{product_name}' foram adicionadas ao carrinho."
        except httpx.HTTPStatusError as e:
            return f"Erro ao adicionar o item: O serviço retornou o status {e.response.status_code}."
        except httpx.RequestError:
            return "Erro de comunicação com o serviço de carrinho de compras."