FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1 

RUN apt-get update && apt-get install -y \
    gcc python3-dev libpq-dev curl \
    && rm -rf /var/lib/apt/lists/*

RUN pip install -U pip pdm

WORKDIR /app

COPY pyproject.toml pdm.lock /app/

# Forçamos a criação da venv dentro de /app/.venv
RUN pdm config python.use_venv true && \
    pdm install --prod --frozen-lockfile --no-editable

COPY . /app/

# Adicionamos a venv no PATH para o Python achar o Django
ENV PATH="/app/.venv/bin:$PATH"

EXPOSE 19003

CMD ["python", "manage.py", "runserver", "0.0.0.0:19003"]