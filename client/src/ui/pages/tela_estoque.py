import flet as ft

# Função que irá criar a tela de estoque:
def criar_tela_estoque(produtos, page):
    # Tabela dos itens em estoque:
    tabela_estoque = ft.DataTable(
        columns=[ # Define as 6 colunas que terão dados (Código, Nome, Preço de custo, Preço de venda, Quantidade e Validade)
            ft.DataColumn(ft.Text("Código")),
            ft.DataColumn(ft.Text("Nome")),
            ft.DataColumn(ft.Text("Preço de custo")),
            ft.DataColumn(ft.Text("Preço de venda")),
            ft.DataColumn(ft.Text("Quantidade")),
            ft.DataColumn(ft.Text("Validade")),
        ],

        rows=[] # As linhas começam vazias, sem nenhum item em estoque
    )

    # Função que adicionará itens à tabela de estoque:
    def atualizar(): 
        tabela_estoque.rows.clear() # Limpa todas as tabelas anteriores para atualizar tudo do zero.

        for p in produtos: # Para cada indice da lista "produtos"
            tabela_estoque.rows.append( # Cria uma nova linha na tabela
                ft.DataRow( # Cada linha/row (neste caso DataRow por ser a linha de uma tabela) é feita de várias células (DataCell), uma para cada coluna.
                    cells=[
                        ft.DataCell(ft.Text(p["codigo"])), # Busca o valor atráves do nome no dicionário da função adicionar produto.
                        ft.DataCell(ft.Text(p["nome"])),
                        ft.DataCell(ft.Text(p["preco_custo"])),
                        ft.DataCell(ft.Text(p["preco_venda"])),
                        ft.DataCell(ft.Text(p["quantidade"])),
                        ft.DataCell(ft.Text(p["validade"])),
                    ]
                )
            ) 

        page.update() # Atualiza a página para mostrar as alterações.

    atualizar()


    # Tela de estoque:
    return ft.Container(
        content=ft.Column(
            [
                ft.Text("Produtos Cadastrados", size=20, weight="bold"),
                tabela_estoque,
            ],
            spacing=10,
        ),

        expand=True,
        bgcolor=ft.Colors.WHITE,
        margin=0,
        padding=20,
        border_radius=15,
        alignment=ft.alignment.center
    )
    