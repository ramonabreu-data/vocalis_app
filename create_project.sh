#!/bin/bash

# Nome do diretório raiz do projeto
PROJECT_NAME="vocalis-challenge"

# --- Criação da Estrutura (idêntica à anterior) ---
echo "Criando o diretório raiz do projeto: $PROJECT_NAME..."
mkdir -p "$PROJECT_NAME"
cd "$PROJECT_NAME" || exit

echo "Criando todas as pastas..."
mkdir -p \
  .vscode \
  docs \
  services/shopping_cart_api/app \
  src/api/v1/endpoints \
  src/agent/tools \
  src/core \
  src/services \
  src/tasks \
  tests/agent \
  tests/api

echo "Criando todos os arquivos vazios..."
touch \
  .vscode/settings.json \
  docs/architecture.md \
  services/shopping_cart_api/app/__init__.py \
  services/shopping_cart_api/app/main.py \
  services/shopping_cart_api/app/models.py \
  services/shopping_cart_api/app/crud.py \
  services/shopping_cart_api/Dockerfile \
  src/__init__.py \
  src/main.py \
  src/api/__init__.py \
  src/api/v1/__init__.py \
  src/api/v1/endpoints/__init__.py \
  src/api/v1/endpoints/vocalis_websocket.py \
  src/api/v1/api.py \
  src/agent/__init__.py \
  src/agent/tools/__init__.py \
  src/agent/tools/shopping_cart.py \
  src/agent/vocalis_agent.py \
  src/core/__init__.py \
  src/core/celery_app.py \
  src/core/config.py \
  src/services/__init__.py \
  src/services/stt.py \
  src/services/tts.py \
  src/tasks/__init__.py \
  src/tasks/handoff.py \
  tests/__init__.py \
  tests/agent/__init__.py \
  tests/agent/test_shopping_cart_tool.py \
  tests/api/__init__.py \
  tests/api/test_vocalis_websocket.py \
  tests/conftest.py \
  .env.example \
  .gitignore \
  docker-compose.yml \
  Dockerfile \
  poetry.lock \
  pyproject.toml \
  README.md

# --- Configuração de Permissões Seguras ---
echo "Aplicando permissões seguras e recomendadas..."
find . -type d -exec chmod 755 {} +
find . -type f -exec chmod 644 {} +

echo "--------------------------------------------------------"
echo "✅ Estrutura de pastas e arquivos criada com sucesso!"
echo "📍 Você está em: $(pwd)"
echo "🔒 Permissões seguras foram definidas (755 para pastas, 644 para arquivos)."