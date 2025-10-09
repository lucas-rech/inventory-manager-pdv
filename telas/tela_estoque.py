from flet import *

# Função que irá criar a tela de estoque:
def criar_tela_estoque(produtos, page):
    # Tabela dos itens em estoque:
    tabela_estoque = DataTable(
        columns=[ # Define as 6 colunas que terão dados (Código, Nome, Preço de custo, Preço de venda, Quantidade e Validade)
            DataColumn(Text("Código")),
            DataColumn(Text("Nome")),
            DataColumn(Text("Preço de custo")),
            DataColumn(Text("Preço de venda")),
            DataColumn(Text("Quantidade")),
            DataColumn(Text("Validade")),
        ],

        rows=[] # As linhas começam vazias, sem nenhum item em estoque
    )

    # Função que adicionará itens à tabela de estoque:
    def atualizar(): 
        tabela_estoque.rows.clear() # Limpa todas as tabelas anteriores para atualizar tudo do zero.

        for p in produtos: # Para cada indice da lista "produtos"
            tabela_estoque.rows.append( # Cria uma nova linha na tabela
                DataRow( # Cada linha/row (neste caso DataRow por ser a linha de uma tabela) é feita de várias células (DataCell), uma para cada coluna.
                    cells=[
                        DataCell(Text(p["codigo"])), # Busca o valor atráves do nome no dicionário da função adicionar produto.
                        DataCell(Text(p["nome"])),
                        DataCell(Text(p["preco_custo"])),
                        DataCell(Text(p["preco_venda"])),
                        DataCell(Text(p["quantidade"])),
                        DataCell(Text(p["validade"])),
                    ]
                )
            ) 

        page.update() # Atualiza a página para mostrar as alterações.

    atualizar()


    # Tela de estoque:
    return Container(
        padding=20,
        expand=True,
        content=Column(
            [
                Text("Produtos Cadastrados", size=20, weight="bold"),
                tabela_estoque,
            ],
            spacing=10,
        ),
    )
    