# ⚙️ Server - Inventory Manager PDV

Backend da aplicação desenvolvido em **Java 17** com **Spring Boot**, fornecendo uma API RESTful para o sistema de gerenciamento.

## 📁 Estrutura Técnica

O projeto segue a arquitetura padrão do Spring Boot. O código fonte principal está em `src/main/java/edu/ifrs/si/inventorymanagerpdv`.

- **`controller/`**: Camada de controladores REST. Recebe as requisições HTTP e retorna as respostas.
- **`service/`**: Camada de serviço. Contém as regras de negócio da aplicação.
- **`repository/`**: Camada de persistência. Interfaces que estendem `CrudRepository` ou `JpaRepository` para acesso ao banco de dados.
- **`model/`**: Entidades do domínio que representam as tabelas do banco de dados.
- **`config/`**: Classes de configuração do Spring (Segurança, CORS, Banco de Dados).

## 🛠️ Tecnologias

- **Java 17**
- **Spring Boot 3.5.7**
- **Spring Data JDBC**
- **Spring Security**
- **H2 Database** (Banco em memória para desenvolvimento)
- **Gradle** (Gerenciador de dependências e build)

## 🚀 Como Rodar

Certifique-se de ter o **JDK 17** instalado e configurado.

### Windows

Abra o terminal na pasta `server` e execute:

```powershell
.\gradlew.bat bootRun
```

### Linux / macOS

Dê permissão de execução ao script e rode:

```bash
chmod +x gradlew
./gradlew bootRun
```

A aplicação iniciará por padrão na porta `8080`.
