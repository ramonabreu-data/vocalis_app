# Use uma imagem base slim para um tamanho menor
FROM python:3.11-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Define variáveis de ambiente para configurar o Poetry
# Isso evita a necessidade de usar 'poetry config' no comando RUN
ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false

# Instala o Poetry no sistema
RUN pip install poetry

# Copia apenas os arquivos de dependência primeiro
# Isso aproveita o cache do Docker. A instalação só será executada novamente
# se o pyproject.toml ou o poetry.lock mudarem.
COPY poetry.lock pyproject.toml ./

# Instala as dependências de produção
RUN poetry install --no-root --without dev

# Agora, copia o código fonte da sua aplicação
COPY ./src ./src

# Expõe a porta que a aplicação vai rodar
EXPOSE 8000

# Define o comando padrão para iniciar a aplicação quando o container rodar.
# Este comando pode ser sobrescrito pelo docker-compose.yml, mas é uma boa prática tê-lo aqui.
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
