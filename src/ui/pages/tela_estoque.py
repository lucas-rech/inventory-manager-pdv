import flet as ft

# Função que irá criar a tela de estoque:
def criar_tela_estoque(produtos, page):
    # Tabela dos itens em estoque:
    tabela_estoque = ft.DataTable(
        columns=[ # Define as 6 colunas que terão dados (Código, Nome, Preço de custo, Preço de venda, Quantidade e Validade)
            ft.DataColumn(ft.Text("Código de Barras", size=18)),
            ft.DataColumn(ft.Text("Nome", size=18)),
            ft.DataColumn(ft.Text("Preço de custo", size=18)),
            ft.DataColumn(ft.Text("Preço de venda", size=18)),
            ft.DataColumn(ft.Text("Quantidade", size=18)),
            ft.DataColumn(ft.Text("Validade", size=18)),
            ft.DataColumn(ft.Text("Ações", size=18))
        ],

        rows=[], # As linhas começam vazias, sem nenhum item em estoque.

        width=1500,
    )

    # Função que adicionará itens à tabela de estoque:
    def atualizar(): 
        tabela_estoque.rows.clear() # Limpa todas as tabelas anteriores para atualizar tudo do zero.

        for i, produto in enumerate(produtos): # Para cada indice da lista "produtos"

            if produto.get("editando", False):
                campo_codigo_barras = ft.TextField(
                    label="Código de Barras",
                    value=produto["codigo"],
                    width=100,
                )

                campo_nome_produto = ft.TextField(
                    label="Nome:",
                    width=120,
                    value=produto["nome"],
                )

                campo_preco_custo = ft.TextField(
                    label="Preço de Custo:",
                    width=120,
                    value=produto["preco_custo"],
                )

                campo_preco_venda = ft.TextField(
                    label="Preço de Venda:",
                    value=produto["preco_venda"],
                    width=120,
                )

                campo_quantidade = ft.TextField(
                    label="Quantidade:",
                    value=produto["quantidade"],
                    width=100,
                )

                campo_validade = ft.TextField(
                    label="Validade:",
                    value=produto["validade"],
                    width=120,
                )

                botao_salvar = ft.TextButton(
                    text="Salvar",
                    style=ft.ButtonStyle(color="#507656"),
                    on_click=lambda e, index=i: salvar(index, campo_codigo_barras, campo_nome_produto, campo_preco_custo, campo_preco_venda, campo_quantidade, campo_validade)
                )

                botao_cancelar = ft.TextButton(
                    text="Cancelar",
                    style=ft.ButtonStyle(color="#9B3E3E"),
                )

                tabela_estoque.rows.append(
                    ft.DataRow( # IMPORTANTE: É obrigatório passar a mesma quantidade de datacells em relação à quantidade de colunas.
                        cells=[
                            ft.DataCell(campo_codigo_barras),
                            ft.DataCell(campo_nome_produto),
                            ft.DataCell(campo_preco_custo),
                            ft.DataCell(campo_preco_venda),
                            ft.DataCell(campo_quantidade),
                            ft.DataCell(campo_validade),
                            ft.DataCell(ft.Row([botao_salvar, botao_cancelar])),
                        ]
                    )
                )

            else:
                botao_editar = ft.TextButton(
                    text="Editar", # Texto escrito no botão.
                    style=ft.ButtonStyle(color="#507656"), # Cor do texto.
                    on_click=lambda e, index=i: editar(index), # Quando for clicado: passa o valor de i par ao parâmetro index da função editar e chama a função editar.
                )

                botao_excluir = ft.TextButton(
                    text="Excluir", # Texto escrito no botão
                    style=ft.ButtonStyle(color="#9B3E3E"), # Cor do texto.
                    on_click=lambda e, index=i: excluir(index) # Quando for clicado: passa o valor de i par ao parâmetro index da função editar e chama a função excluir.
                )
                
                tabela_estoque.rows.append( # Cria uma nova linha na tabela

                    ft.DataRow( # Cada linha/row (neste caso DataRow por ser a linha de uma tabela) é feita de várias células (DataCell), uma para cada coluna.
                        cells=[
                            ft.DataCell(ft.Text(produto["codigo"], size=16)), # Busca o valor atráves do nome no dicionário da função adicionar produto.
                            ft.DataCell(ft.Text(produto["nome"], size=16)),
                            ft.DataCell(ft.Text(produto["preco_custo"], size=16)),
                            ft.DataCell(ft.Text(produto["preco_venda"], size=16)),
                            ft.DataCell(ft.Text(produto["quantidade"], size=16)),
                            ft.DataCell(ft.Text(produto["validade"], size=16)),
                            ft.DataCell(ft.Row([botao_editar, botao_excluir])),
                        ]
                    )
                ) 

        page.update() # Atualiza a página para mostrar as alterações.

    atualizar()

    # FUNÇÕES DE EDIÇÃO DA TABELA:
    # Função de editar dados da tabela:
    def editar(index): # Recebe o index dos dados que serão editados.
        produtos[index]["editando"] = True # Altera o valor de editando no index passado para "True".
        atualizar() # Atualiza a tabela.

    # Função de excluir dados da tabela:
    def excluir(index): # Recebe o index dos dados que serão excluidos.
        produtos.pop(index) # Exclui o item contido no index.
        atualizar() # Atualiza a tabela.

    # Função de salar os novos dados na tabela:
    def salvar(index, campo_codigo_barras, campo_nome_produto, campo_preco_custo, campo_preco_venda, campo_quantidade, campo_validade):
        produtos[index]["codigo"] = campo_codigo_barras.value
        produtos[index]["nome"] = campo_nome_produto.value
        produtos[index]["preco_custo"] = campo_preco_custo.value
        produtos[index]["preco_venda"] = campo_preco_venda.value
        produtos[index]["quantidade"] = campo_quantidade.value
        produtos[index]["validade"] = campo_validade.value
        produtos[index]["editando"] = False
        atualizar()

    # Container que conterá a tabela de clientes (Ajudará a viabilizar algumas funções como o scroll e fixar o título no topo da tabela)
    container_tabela = ft.Container(
        content=ft.Column(
            [tabela_estoque],
            scroll=ft.ScrollMode.AUTO # Habilita o scroll automaticamente quando a altura máxima é atingida.
        ),

        expand=True,
        border=ft.border.all(2, color="#765070"),
        border_radius=10,
    )

    # Tela de estoque:
    return ft.Container(
        content=ft.Column(
            [
                ft.Text("Produtos Cadastrados", size=30, weight="bold"),
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
    