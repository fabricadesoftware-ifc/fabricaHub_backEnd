FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1 

# Instala dependências do sistema
RUN apt-get update && apt-get install -y \
    gcc python3-dev libpq-dev curl \
    && rm -rf /var/lib/apt/lists/*

RUN pip install -U pip pdm

WORKDIR /app

# Copia os arquivos de dependências a partir da raiz do projeto
COPY pyproject.toml pdm.lock /app/

# GARANTE A VENV: O PDM vai criar a venv isolada em /app/.venv
RUN pdm config python.use_venv true && \
    pdm install --prod --frozen-lockfile --no-editable

# Copia o restante do código da raiz do projeto para dentro de /app
COPY . /app/

# Adiciona o bin da venv e os site-packages ao PATH/PYTHONPATH do container
ENV PATH="/app/.venv/bin:$PATH"
ENV PYTHONPATH="/app/.venv/lib/python3.12/site-packages"

EXPOSE 19003

# Executa o servidor direto pelo ambiente correto
CMD ["python", "manage.py", "runserver", "0.0.0.0:19003"]