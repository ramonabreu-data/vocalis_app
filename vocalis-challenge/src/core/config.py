from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Para carregar variáveis do arquivo .env
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    # Chave de API para o provedor de LLM (ex: OpenAI, Groq, Anthropic)
    OPENAI_API_KEY: str

    # URL base do nosso microserviço de carrinho de compras
    SHOPPING_CART_API_URL: str = "http://shopping-cart-api:8001"


# Instância única que será importada em outras partes do código
settings = Settings()