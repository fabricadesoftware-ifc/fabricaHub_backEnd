# FábricaHub

Sistema institucional da Fábrica de Software responsável pela gestão de membros, projetos, squads, certificados, comunicação, integrações e gestão do conhecimento.

---

# Visão Geral

O FábricaHub será o backend central da Fábrica de Software.

A plataforma será responsável por:

* Gestão de membros
* Gestão de projetos
* Gestão de squads
* Histórico de participação
* Geração de certificados
* Integração com portal público
* Integração com controle de acesso via ESP
* Integração com GitHub
* Comunicação entre squads
* Notificações PWA
* Gestão do conhecimento com IA/RAG

---

# Arquitetura Geral

```text
                ┌──────────────────────┐
                │   Frontend Admin     │
                │     Vue 3 + PWA      │
                └──────────┬───────────┘
                           │
                           │ REST API
                           │
                ┌──────────▼───────────┐
                │    FábricaHub API    │
                │ Django REST Backend  │
                └──────────┬───────────┘
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
        ▼                  ▼                  ▼
 PostgreSQL           Redis/Celery        Firebase
                                           FCM
        │
        ├─────────────── GitHub API
        ├─────────────── ESP Access Control
        ├─────────────── Portal Público
        └─────────────── IA/RAG
```

---

# Estrutura do Projeto

```text
fabricahub/
│
├── backend/
│   ├── apps/
│   ├── core/
│   ├── config/
│   ├── requirements/
│   ├── docker/
│   └── manage.py
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── tests/
│   └── vite.config.js
│
├── docker-compose.yml
├── README.md
└── .env.example
```

---

# Backend

## Stack

* Python
* Django
* Django REST Framework
* PostgreSQL
* Redis
* Celery
* Pytest
* Docker
* GitHub Actions

---

# Objetivo do Backend

O backend será responsável por:

* Centralizar os dados da Fábrica
* Expor APIs públicas e privadas
* Controlar permissões
* Integrar com GitHub
* Integrar com ESPs
* Gerar certificados
* Registrar histórico
* Gerenciar notificações
* Alimentar o portal público
* Alimentar o sistema de IA

---

# Estrutura Backend

```text
backend/
│
├── apps/
│   ├── members/
│   ├── projects/
│   ├── squads/
│   ├── technologies/
│   ├── certificates/
│   ├── communication/
│   ├── access_control/
│   ├── github_integration/
│   ├── notifications/
│   ├── knowledge/
│   └── public_api/
│
├── core/
│   ├── permissions/
│   ├── authentication/
│   ├── activity_logs/
│   ├── events/
│   └── utils/
│
├── config/
│   ├── settings/
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
└── manage.py
```

---

# Principais Módulos Backend

## Members

Responsável pela gestão de membros da Fábrica.

### Funcionalidades

* Cadastro de membros
* Tipos de membros
* Status
* Histórico
* Tecnologias dominadas
* Perfil público

---

## Projects

Responsável pelos projetos desenvolvidos.

### Funcionalidades

* Cadastro de projetos
* Tecnologias utilizadas
* Status
* Squad responsável
* Integração GitHub
* Dados públicos

---

## Squads

Responsável pela organização das equipes.

### Funcionalidades

* Cadastro de squads
* Organização por projeto
* Papéis dos membros
* Histórico de participação

---

## Certificates

Responsável pela geração e validação de certificados.

### Funcionalidades

* Templates
* Geração de PDF
* Código de verificação
* Página pública de validação
* Controle de carga horária

---

## Communication

Responsável pela comunicação interna.

### Funcionalidades

* Discussões por tópico
* Chat em tempo real
* Decisões técnicas
* Menções
* Histórico de mensagens

---

## Access Control

Responsável pela integração com ESPs.

### Funcionalidades

* Controle de tags
* Logs de acesso
* Autorização de entrada
* Registro de dispositivos
* Integração REST com ESP32

---

## GitHub Integration

Responsável pela integração com GitHub.

### Funcionalidades

* Criar issues
* Criar branches
* Sincronizar PRs
* Registrar commits
* Receber webhooks
* Dashboard de atividade

---

## Knowledge

Responsável pela gestão do conhecimento.

### Funcionalidades

* Indexação de documentos
* IA para onboarding
* IA para gestão
* RAG
* Busca semântica

---

# API

## API Privada

Consumida por:

* Frontend administrativo
* PWA
* Comunicação interna
* IA

Exemplos:

```text
/api/members/
/api/projects/
/api/squads/
/api/certificates/
/api/github/
/api/access-control/
```

---

## API Pública

Consumida pelo portal público.

Exemplos:

```text
/public/projects/
/public/members/
/public/technologies/
/public/certificates/verify/{code}/
```

---

# Activity Logs

O sistema terá logs centralizados.

Exemplos:

* membro criado
* projeto criado
* issue criada
* acesso autorizado
* certificado emitido
* mensagem enviada

---
