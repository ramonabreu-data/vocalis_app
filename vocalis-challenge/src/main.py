from fastapi import FastAPI
from src.api.v1.api import api_router

app = FastAPI(title="Vocalis Main Backend")

@app.get("/health")
def read_root():
    return {"status": "ok"}

# Inclui todas as rotas da v1 sob o prefixo /api/v1
app.include_router(api_router, prefix="/api/v1")