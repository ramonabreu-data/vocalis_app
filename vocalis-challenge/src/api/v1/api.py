from fastapi import APIRouter
from src.api.v1.endpoints import vocalis_websocket

api_router = APIRouter()
api_router.include_router(vocalis_websocket.router, tags=["Vocalis WebSocket"])