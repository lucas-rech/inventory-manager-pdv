import flet as ft

def criar_tela_clientes(clientes, page):
    tabela_clientes = ft.DataTable(
        columns=[ # Define as 2 colunas que terão dados (Nome, Número)
            ft.DataColumn(ft.Text("Nome")),
            ft.DataColumn(ft.Text("Número de Telefone")),
            ft.DataColumn(ft.Text("CPF / CNPJ"))
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
                        ft.DataCell(ft.Text(c["numero"])),
                        ft.DataCell(ft.Text(c["cpf_cnpj"]))
                    ]
                )
            )

        page.update()

    atualizar()

    # Container que conterá a tabela de clientes (Ajudará a viabilizar algumas funções como o scroll e fixar o título no topo da tabela)
    container_tabela = ft.Container(
        content=ft.Column(
            [tabela_clientes],
            scroll=ft.ScrollMode.AUTO, # Habilita o scroll automaticamente quando a altura máxima é atingida.
        ),

        expand=True, # Altura máxima
        border=ft.border.all(2, color="#765070"),
        border_radius=10
    )

    return ft.Container(
        content=ft.Column(
            [
                ft.Text("Clientes Cadastrados", size=20, weight="bold"),
                container_tabela,
            ],
            spacing=10,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),

        expand=True,
        bgcolor=ft.Colors.WHITE,
        margin=0,
        padding=20,
        border_radius=15,
        alignment=ft.alignment.center,
    )
