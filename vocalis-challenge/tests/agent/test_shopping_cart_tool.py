import pytest
import httpx
import respx

from src.agent.tools.shopping_cart import add_item_to_cart
from src.core.config import settings

@pytest.mark.asyncio
@respx.mock
async def test_add_item_to_cart_success():
    # Define uma rota mockada. Quando a ferramenta tentar fazer um POST para esta URL...
    user_id = "user123"
    url = f"{settings.SHOPPING_CART_API_URL}/cart/{user_id}/items"

    # ...o respx irá interceptar e retornar esta resposta, sem fazer uma chamada de rede real.
    respx.post(url).mock(return_value=httpx.Response(200, json={
        "user_id": user_id,
        "items": [{"product_name": "café", "quantity": 2}]
    }))

    # Chama a ferramenta com os argumentos
    result = await add_item_to_cart.ainvoke({
        "product_name": "café",
        "quantity": 2
    })

    # Verifica se a resposta em linguagem natural está correta
    assert "Sucesso" in result
    assert "2 unidade(s) de 'café' foram adicionadas" in result