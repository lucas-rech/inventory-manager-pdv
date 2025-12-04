# Inventory Manager PDV

Sistema de gerenciamento de inventário e ponto de venda (PDV) para mercados.

## 📁 Estrutura do Projeto

O projeto é dividido em dois diretórios principais: `client` e `server`.

### 🖥️ Client (Frontend/Desktop App)

O cliente é uma aplicação desktop desenvolvida em **Python** utilizando o framework **Flet**, que permite a criação de interfaces gráficas modernas e multiplataforma.

**Principais Tecnologias e Bibliotecas:**
- **Flet**: Framework principal para construção da interface do usuário.
- **screeninfo**: Biblioteca utilizada para obter informações sobre os monitores conectados.
- **validate-docbr**: Biblioteca para validação de documentos brasileiros (CPF, CNPJ).

**Estrutura de Diretórios (`client/src`):**
- `main.py`: Ponto de entrada da aplicação.
- `app/`: Contém a lógica de negócios da aplicação.
- `ui/`: Contém os componentes visuais e as páginas da interface (telas de cadastro, estoque, PDV, etc.).
- `assets/`: Armazena recursos estáticos como imagens e ícones.

### ⚙️ Server (Backend)

O servidor é desenvolvido em **Java 17** utilizando o framework **Spring Boot**, responsável por gerenciar a lógica de negócios, persistência de dados e segurança.

**Principais Tecnologias e Bibliotecas:**
- **Spring Boot 3.5.7**: Framework base para desenvolvimento da aplicação.
- **Spring Web**: Módulo para criação de APIs RESTful.
- **Spring Data JDBC**: Abstração para acesso a dados e persistência.
- **Spring Security**: Framework de autenticação e controle de acesso.
- **H2 Database**: Banco de dados em memória utilizado em ambiente de desenvolvimento/runtime.
- **Gradle**: Ferramenta de automação de build e gerenciamento de dependências.

**Estrutura de Diretórios (`server`):**
- `src/main/java`: Código fonte da aplicação Java.
- `build.gradle`: Arquivo de configuração do Gradle, definindo plugins e dependências.
