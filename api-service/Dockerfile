FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y build-essential && rm -rf /var/lib/apt/lists/*

RUN pip install poetry

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-ansi --only main

COPY . .

CMD ["sh", "-c", "uvicorn src.serving.main:app --host 0.0.0.0 --port $PORT"]

