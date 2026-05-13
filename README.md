
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

Certifique-se de ter o Python 3.12 instalado. Se ainda não possui o PDM, instale-o:

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
#### 1. Inicialize o Postgres e o Redis:

```
docker compose up -d
```
#### 2. Para inicializar a aplicação basta usar:

```
pdm run dev
```
> Observação: Ira rodar o script/set_my_ip.py e gravando seu IP no .env para o settings/base.py saber qual IP liberar durante o desenvolvimento ( porta 19003 por padrão)
