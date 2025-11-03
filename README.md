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
│   ├── config/                                # Arquivos de configuração
│   │
│   ├── modules/
│   │   └── clientes/
│   │       ├── cliente.entity.ts              # Entidade de cliente
│   │       └── cliente.repository.ts          # Repositório que entra em contato com o db
│   │       └── cliente.service.ts             # Regras de negócio de clientes
│   │   └── common/
│   │       ├── base.entity.ts                 # Entidade abstrata
│   │       └── enums.ts                       # Enums
│   │   └── produtos/
│   │           └── lotes/
│   │               ├── lote.entity.ts         # Entidade de lotes
│   │               └── lote.repository.ts     # Repositório customizado que entra em contato com o db
│   │       ├── produto.entity.ts              # Entidade de produtos
│   │       └── produtos.service.ts            # Regras de negócios de produtos
│   │   └── vendas/               
│   │       ├── produto-venda.entity.ts        # Tabela many to many
│   │       └── venda.entity.ts                # Entidade de venda           
│   │
│   └── main.ts                                # Ponto de entrada principal
│
├── .eslintrc.json                             # Configurações do ESLint
├── .prettierrc                                # Configurações do Prettier
├── tsconfig.json                              # Configurações do TypeScript
├── package.json
