FROM python:3.12-slim

# Impede que o Python gere arquivos .pyc e garante logs em tempo real
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1 

# INSTALAÇÃO DE DEPENDÊNCIAS DO SISTEMA
# Precisamos do gcc e libpq-dev para compilar pacotes como netifaces e psycopg2
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Instala o PDM
RUN pip install -U pip setuptools wheel
RUN pip install pdm

# Define o diretório de trabalho
WORKDIR /app

# Configura o PDM para não usar venv dentro do container (opcional, mas evita o erro que você viu)
RUN pdm config python.use_venv false

# Copia apenas os arquivos de dependências primeiro
COPY pyproject.toml pdm.lock /app/

# Instala as dependências (usando --frozen-lockfile pois --no-lock foi depreciado)
RUN pdm install --prod --frozen-lockfile --no-editable

# Copia o restante do código
COPY . /app/

EXPOSE 19003

CMD ["pdm", "run", "dev"]