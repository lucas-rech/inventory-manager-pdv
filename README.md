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


## 🛠️ Tecnologias Utilizadas

| Camada | Tecnologia | Descrição |
|--------|-------------|------------|
| Frontend | [Flet](https://flet.dev/) | Framework Python para interfaces gráficas modernas |
| Backend | [Node.js](https://nodejs.org/) | Plataforma JavaScript para o servidor |
| ORM | [MikroORM](https://mikro-orm.io/) | ORM TypeScript para bancos SQL |
| Framework Web | [Express](https://expressjs.com/) | Framework para APIs REST |
| Banco de Dados | PostgreSQL / SQLite | Persistência relacional dos dados |
| Linguagens | Python, TypeScript | Camadas de apresentação e lógica de negócios |