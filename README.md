<<<<<<< HEAD
# 🧩 Server Boilerplate — TypeScript + Express + MikroORM

Este projeto é a base do servidor escrito em **TypeScript**, utilizando **Express** para o roteamento HTTP e **MikroORM** para o mapeamento objeto-relacional.  
O ambiente de desenvolvimento é padronizado com **ESLint** e **Prettier**, garantindo qualidade e consistência de código.

No banco de dados, utilizamos MySQL.

---

## 🚀 Tecnologias Utilizadas

- **TypeScript** — Tipagem estática para JavaScript.
- **Express** — Framework web minimalista para Node.js.
- **MikroORM** — ORM para TypeScript e Node.js, com suporte a múltiplos bancos.
- **ESLint** — Linter para padronização e boas práticas.
- **Prettier** — Formatador de código.
- **ts-node-dev** — Reinicialização automática durante o desenvolvimento.

---

## 📁 Estrutura do Projeto

```bash
server/
│
├── src/
│   │
│   ├── modules/
│   │   └── clientes/
│   │       ├── cliente.entity.ts  # Exemplo de entidade do MikroORM
│   │       └── example.route.ts   # Exemplo de rota Express
│   │
│   └── server.ts                     # Ponto de entrada principal
│
├── .eslintrc.json                 # Configurações do ESLint
├── .prettierrc                    # Configurações do Prettier
├── tsconfig.json                  # Configurações do TypeScript
├── package.json
=======
# 🧾 Sistema de PDV e Gestão de Estoque

Projeto acadêmico desenvolvido no **Instituto Federal do Rio Grande do Sul (IFRS)** como parte das atividades práticas da disciplina de **Engenharia e Software II / IHC e Sistemas de Informação e Apoio a Decisão**.  
O sistema tem como objetivo **simular o funcionamento de um ponto de venda (PDV)** integrado a um **módulo de gestão de estoque**, permitindo o controle de produtos, clientes e vendas em tempo real.

---

## 🧩 Arquitetura do Projeto

O sistema é dividido em **duas camadas principais**:

### 🖥️ Frontend
- Desenvolvido em **Python** utilizando o framework **[Flet](https://flet.dev/)**.
- Interface desktop moderna e responsiva.
- Comunicação com o backend via **requisições HTTP (REST API)**.
- Foco na simplicidade e na experiência do operador de caixa.

### ⚙️ Backend
- Desenvolvido em **Node.js** com **[Express](https://expressjs.com/)**.
- ORM: **[MikroORM](https://mikro-orm.io/)** para abstração do banco de dados.
- Banco de dados relacional MySQL.
- Fornece endpoints REST para operações de CRUD e controle de estoque.

---

## 🗃️ Estrutura de Pastas
```bash
project-root/
│
├── client/                      # Aplicação Flet (Python)
│   ├── src/
│   │   ├── main.py              # Ponto de entrada da aplicação
│   │   ├── assets/              # Recursos visuais (imagens, ícones, etc.)
│   │   ├── ui/                  # Elementos da interface
│   │   │   ├── components/      # Componentes reutilizáveis da UI
│   │   │   ├── pages/           # Páginas principais da aplicação
│   │   └── services/            # Comunicação com o backend
│   ├── requirements.txt
│   └── README.md
│
├── server/                      # Backend Node.js
│   ├── src/
│   │   ├── modules/             # Módulos do sistema (produtos, vendas, clientes, etc.)
│   │   ├── core/                # Configurações globais (ORM, logger, middlewares)
│   │   ├── app.ts
│   │   └── server.ts
│   ├── mikro-orm.config.ts
│   ├── package.json
│   └── tsconfig.json
│
└── README.md                    # Este arquivo
>>>>>>> 3a0133359c87bb345b81e433fd69f22b1831746d
