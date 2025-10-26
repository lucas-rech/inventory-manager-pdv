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
