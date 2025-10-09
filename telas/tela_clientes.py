import flet as ft

def criar_tela_clientes(clientes, page):
    tabela_clientes = ft.DataTable(
        columns=[ # Define as 2 colunas que terão dados (Nome, Número)
            ft.DataColumn(ft.Text("Nome")),
            ft.DataColumn(ft.Text("Número de Telefone")),
        ],

        rows = [] # As linhas começam vazias, sem nenhum cliente cadstrado.
    )

    # Função que adicionará itens à tabela de estoque:
    def atualizar():
        tabela_clientes.rows.clear() # Limpa todas as tabelas anteriores para atualizar tudo do zero.

        for c in clientes:# Para cada indice da lista "produtos"
            tabela_clientes.rows.append( # Cria uma nova linha na tabela
                ft.DataRow( # Cada linha/row (neste caso DataRow por ser a linha de uma tabela) é feita de várias células (DataCell), uma para cada coluna.
                    cells = [
                        ft.DataCell(ft.Text(c["nome"])), # Busca o valor atráves do nome no dicionário da função adicionar produto.
                        ft.DataCell(ft.Text(c["numero"]))
                    ]
                )
            )

        page.update()

    atualizar()

    return ft.Container(
        padding=20,
        expand=True,
        content=ft.Column(
            [
                ft.Text("Clientes Cadastrados", size=20, weight="bold"),
                tabela_clientes,
            ],
            spacing=10,
        ),
    )
