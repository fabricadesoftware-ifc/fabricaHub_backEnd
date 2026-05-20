# FabricaHub Backend 🚀

![Python](https://img.shields.io/badge/python-3.12-blue)
![Django](https://img.shields.io/badge/django-5.x-green)
![PostgreSQL](https://img.shields.io/badge/postgresql-16-blue)
![Redis](https://img.shields.io/badge/redis-latest-red)
![Docker](https://img.shields.io/badge/docker-latest-blue)
![PDM](https://img.shields.io/badge/pdm-latest-purple)
Esta documentação segue em constante atualização.

---
  
# ⚙️ Configuração do Ambiente



### 📁 Estrutura do Projeto

```bash
core/              # Configurações principais
docker/            # Arquivos Docker
fabricahub/        # Apps Django
```
## 1. Pré-requisitos

Certifique-se de possuir instalado:

- Docker
- Docker Compose

> Python e PDM são necessários apenas para execução sem Docker.

---

## 2. Configuração das Variáveis de Ambiente

Copie o arquivo de exemplo:

```bash
cp .env.example .env
```

> Nunca envie o arquivo `.env` para o repositório.

---

# 🚀 Inicialização com Docker

## 1. Subindo os Containers (Apenas a primeira vez)

```bash
docker compose -p fabricahub -f docker/compose.yml up -d --build
```
> A opção `--build` é necessária apenas na primeira execução para construir as imagens. Em execuções subsequentes, basta usar `docker compose -p fabricahub -f docker/compose.yml up -d`.
A aplicação ficará disponível em:

```txt
http://localhost:19003
```

---

## 2. Verificando os Containers

```bash
docker compose -p fabricahub -f docker/compose.yml ps
```

Containers esperados:

```bash
fabricahub-db-1     # Container do PostgreSQL
fabricahub-redis-1  # Container do Redis
fabricahub-web-1   # Container do Django
```

---

## 3. Aplicando as Migrações

```bash
docker compose -p fabricahub -f docker/compose.yml exec web pdm run migrate
```

---

## 4. Criando Usuário Administrador

```bash
docker compose -p fabricahub -f docker/compose.yml exec web pdm run python manage.py createsuperuser
```
> Por padrão usuario "fabrica" senha "fabrica", email pode deixar vazio.
---

## 5. Acessando Logs

```bash
docker compose -p fabricahub -f docker/compose.yml logs -f
```

> Se deu tudo certo até aqui, a aplicação já deve estar rodando normalmente.
Caso não esteja, você pode iniciar a aplicação sem Docker para facilitar a depuração, seguindo as instruções na seção <a href="#-como-iniciar-o-django-sem-docker">"Como iniciar o Django sem Docker"</a>.


---

# 🛠️ Comandos Úteis

## Parar os Containers

```bash
docker compose -p fabricahub -f docker/compose.yml down
```

---

## Rebuild dos Containers

```bash
docker compose -p fabricahub -f docker/compose.yml up -d --build
```

---

## Executar Shell no Container

```bash
docker compose -p fabricahub -f docker/compose.yml exec web /bin/bash
```

---

# 📄 Exemplo de `.env`

```env
# Django
SECRET_KEY=
DEBUG=True

# Database
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=db
DB_PORT=5432

# Redis
REDIS_HOST=redis
REDIS_PORT=6379
```

---

# 📦 .dockerignore

```dockerignore
.venv
__pycache__
.git
.env
```

---

# 💻 Como iniciar o Django sem Docker

> Utilize este método apenas caso o Docker apresente problemas na execução do 'fabricahub-web-1'.

## 1. Instalar Dependências

Instale o PDM:

```bash
pip install pdm
```

Depois:

```bash
pdm install
```

---

## 2. Ajustar o `.env`

Altere:

```env
DB_HOST=db
```

para:

```env
DB_HOST=localhost
```

---

## 3. Aplicar Migrações

```bash
pdm run migrate
```

---

## 4. Criar Usuário Administrador

```bash
pdm run python manage.py createsuperuser
```

---

## 5. Iniciar o Django

```bash
pdm run dev
```

---

# 🤝 Contribuição

Contribuições são bem-vindas.

Você pode:

- Abrir uma Issue
- Enviar um Pull Request