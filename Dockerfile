FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1 

# Instala dependências do sistema
RUN apt-get update && apt-get install -y \
    gcc python3-dev libpq-dev curl \
    && rm -rf /var/lib/apt/lists/*

RUN pip install -U pip pdm

WORKDIR /app

# Copia apenas os arquivos de dependências primeiro (otimiza cache)
COPY pyproject.toml pdm.lock /app/

# Configura o PDM para instalar na pasta /app/.venv
# IMPORTANTE: --check garante que o lockfile está batendo
RUN pdm config python.use_venv true && \
    pdm install --prod --frozen-lockfile --no-editable

# Copia o restante do código
COPY . /app/

# Adiciona o bin da venv e os site-packages ao PATH/PYTHONPATH
ENV PATH="/app/.venv/bin:$PATH"
ENV PYTHONPATH="/app/.venv/lib/python3.12/site-packages"

EXPOSE 19003

# Recomendação: Use 'pdm run' para garantir que ele use o ambiente correto
CMD ["pdm", "run", "python", "manage.py", "runserver", "0.0.0.0:19003"]