
# FabricaHub_backEnd 🚀

Esta documentação segue em constante atualização.

## Principais Tecnologias
- Python 3.12
- Django 5.x
- PDM (Gerenciador de pacotes e ambientes virtuais)
- PostgreSQL (Banco de dados principal)
- Redis (Cache e mensageria)
## ⚙️ Configuração do Ambiente
#### 1. Pré-requisitos

Certifique-se de ter o Python 3.12 instalado. 
E se você ainda não possuir o PDM instalado, realize a instalação com:

```
pip install pdm
```

#### 2. Instalação de Dependências
Na raiz do projeto execute:

```
pdm install
```

#### 3. Variáveis de Ambiente

```
cp .env.example .env
```
> Nota: Nunca suba o arquivo .env para o repositório.


## 🚀 Inicializacao
#### 1. Vai inicializar nossa aplicação (Django, Postgres e Redis):

```
docker compose up -d
```
> Por padrão nossa aplicação do django se iniciará na porta 19003

- Para você consultar os logs basta utilizar no mesmo diretório:
```
docker compose logs
```