# 🖥️ Client - Inventory Manager PDV

Aplicação desktop desenvolvida em **Python** com **Flet** para o gerenciamento de inventário e ponto de venda.

## 📁 Estrutura Técnica

O código fonte encontra-se no diretório `src/` e está organizado da seguinte forma:

- **`main.py`**: Ponto de entrada da aplicação. Configura a janela principal e inicia o loop de eventos do Flet.
- **`ui/`**: Contém a camada de interface do usuário.
    - **`pages/`**: Telas completas da aplicação (Login, PDV, Estoque, Cadastro).
    - **`components/`**: Componentes reutilizáveis (Botões, Inputs, Headers, Menus).
- **`app/`**: Contém a lógica de negócios e classes auxiliares.
- **`assets/`**: Recursos estáticos como imagens, ícones e fontes.

## 🚀 Como Rodar

Certifique-se de ter o **Python 3.9+** instalado.

### Usando `uv` (Recomendado)

Se você utiliza o gerenciador de pacotes `uv`:

1.  Instale as dependências e rode a aplicação:
    ```bash
    uv run flet run src/main.py
    ```

### Usando `Poetry`

1.  Instale as dependências:
    ```bash
    poetry install
    ```
2.  Rode a aplicação:
    ```bash
    poetry run flet run src/main.py
    ```

### Usando `pip` padrão

1.  Crie um ambiente virtual (opcional mas recomendado):
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # Linux/Mac
    .venv\Scripts\activate     # Windows
    ```
2.  Instale as dependências:
    ```bash
    pip install flet screeninfo validate-docbr
    ```
3.  Rode a aplicação:
    ```bash
    flet run src/main.py
    ```