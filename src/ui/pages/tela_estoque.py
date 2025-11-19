import flet as ft
import re

# Função que irá criar a tela de estoque:
def criar_tela_estoque(produtos, page):
    # Tabela dos itens em estoque:
    tabela_estoque = ft.DataTable(
        columns=[ # Define as 6 colunas que terão dados (Código, Nome, Preço de custo, Preço de venda, Quantidade e Validade)
            ft.DataColumn(ft.Text("Código de Barras", size=16)),
            ft.DataColumn(ft.Text("Nome", size=16)),
            ft.DataColumn(ft.Text("Preço de custo", size=16)),
            ft.DataColumn(ft.Text("Preço de venda", size=16)),
            ft.DataColumn(ft.Text("Quantidade", size=16)),
            ft.DataColumn(ft.Text("Validade", size=16)),
            ft.DataColumn(ft.Text("Ações", size=16))
        ],

        rows=[], # As linhas começam vazias, sem nenhum item em estoque.

        width=1500,
    )

    # Função que adicionará itens à tabela de estoque:
    def atualizar(): 
        tabela_estoque.rows.clear() # Limpa todas as tabelas anteriores para atualizar tudo do zero.

        for i, produto in enumerate(produtos): # Para cada indice da lista "produtos"

            if produto.get("editando", False):
                global campo_codigo_barras
                campo_codigo_barras = ft.TextField(
                    label="Código de Barras",
                    value=produto["codigo"],
                    width=100,
                    on_change=formatar_codigo_barras,
                )

                global campo_nome_produto
                campo_nome_produto = ft.TextField(
                    label="Nome:",
                    width=120,
                    value=produto["nome"],
                    on_change=formatar_nome_produto,
                )

                global campo_preco_custo
                campo_preco_custo = ft.TextField(
                    label="Preço de Custo:",
                    width=120,
                    value=produto["preco_custo"],
                    on_change=formatar_preco_custo,
                )

                campo_preco_venda = ft.TextField( # Terminar a formatação deste campo
                    label="Preço de Venda:",
                    value=produto["preco_venda"],
                    width=120,
                )

                global campo_quantidade
                campo_quantidade = ft.TextField(
                    label="Quantidade:",
                    value=produto["quantidade"],
                    width=100,
                    on_change=formatar_quantidade,
                )

                global campo_validade
                campo_validade = ft.TextField(
                    label="Validade:",
                    value=produto["validade"],
                    width=120,
                    on_change=formatar_validade,
                )

                botao_salvar = ft.TextButton(
                    text="Salvar",
                    style=ft.ButtonStyle(color="#507656"),
                    on_click=lambda e, index=i: salvar(index, campo_codigo_barras, campo_nome_produto, campo_preco_custo, campo_preco_venda, campo_quantidade, campo_validade)
                )

                botao_cancelar = ft.TextButton(
                    text="Cancelar",
                    style=ft.ButtonStyle(color="#9B3E3E"),
                    on_click=lambda e, index=i: cancelar(index),
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
                            ft.DataCell(ft.Text(produto["codigo"], size=14)), # Busca o valor atráves do nome no dicionário da função adicionar produto.
                            ft.DataCell(ft.Text(produto["nome"], size=14)),
                            ft.DataCell(ft.Text(produto["preco_custo"], size=14)),
                            ft.DataCell(ft.Text(produto["preco_venda"], size=14)),
                            ft.DataCell(ft.Text(produto["quantidade"], size=14)),
                            ft.DataCell(ft.Text(produto["validade"], size=14)),
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

    janela_editar = ft.AlertDialog(
        title=ft.Text("Editar", weight="bold", text_align=ft.TextAlign.CENTER),

        content=ft.Container(
            content=ft.Column(
                controls=[
                    ft.ResponsiveRow(
                        controls=[
                            ft.Container(),
                        ],
                    ),
                ],
            ),
        ),
    )

    # Função de excluir dados da tabela:
    def excluir(index): # Recebe o index dos dados que serão excluidos.
        produtos.pop(index) # Exclui o item contido no index.
        atualizar() # Atualiza a tabela.

    # Função de salvar os novos dados na tabela:
    def salvar(index, campo_codigo_barras, campo_nome_produto, campo_preco_custo, campo_preco_venda, campo_quantidade, campo_validade): # Recebe os campos que recebem as novas informações.
        produtos[index]["codigo"] = campo_codigo_barras.value # Muda o dado contido na chave codigo, no index passado.
        produtos[index]["nome"] = campo_nome_produto.value # Muda o dado contido na chave nome, no index passado.
        produtos[index]["preco_custo"] = campo_preco_custo.value # Muda o dado contido na chave preco_custo, no index passado.
        produtos[index]["preco_venda"] = campo_preco_venda.value # Muda o dado contido na chave preco_venda, no index passado.
        produtos[index]["quantidade"] = campo_quantidade.value # Muda o dado contido na chave quantidade, no index passado.
        produtos[index]["validade"] = campo_validade.value # Muda o dado contido na chave validade, no index passado.
        produtos[index]["editando"] = False # Muda o valor contido na chave editando, no index passado.
        atualizar() # Atualiza a tabela.

    # Função que irá cancelar as alterações:
    def cancelar(index): # Recebe o index de onde a alteração está sendo feita.
        produtos[index]["editando"] = False # Muda o valor contido na chave editando, no index passado.
        atualizar() # Atualiza a tabela.







    # FUNÇÕES DE FORMATAÇÃO DOS DADOS DA TABELA: 
    def formatar_codigo_barras(e):
        texto = "".join(filter(str.isdigit, e.control.value))
        campo_codigo_barras.value = texto
        page.update()

    def formatar_nome_produto(e):
        texto = e.control.value

        if re.fullmatch(r"[A-Za-zÀ-ÿ ]*", texto): # Verifica se os caracteres contidos em "texto" casam com o filtro especificado (A até Z, a até Z, letras com acentos e espaços).
            campo_nome_produto.error_text = None

        else: # Se não bater com o filtro
            campo_nome_produto.error_text = "Apenas letras!"

        campo_nome_produto.value = re.sub(r"\s{2,}", " ", texto)
        page.update()

    def formatar_preco_custo(e):
        texto = "".join(filter(str.isdigit, e.control.value))

        if not texto:
            campo_preco_custo.value = "R$ 0,00"
            page.update()
            return # O return está vazio aqui para quefuncione como um "Break" da função, ou seja para aqui.

        # Converte para inteiro e divide por 100 para colocar vírgula decimal
        valor = int(texto) / 100

        # Formata com separador de milhar (.) e decimal (,)
        formatado = f"R$ {valor:.2f}".replace(",", "v").replace(".", ",").replace("v", ".") # A ideia aqui é usar uma letra provisória (v) pra segurar o lugar das vírgulas, e só depois trocar tudo certinho.
        # essa troca dupla inverte o padrão americano (1,234.56 → 1.234,56)

        campo_preco_custo.value = formatado
        page.update()

    def formatar_quantidade(e):
        texto = "".join(filter(str.isdigit, e.control.value))
        texto = texto[:5]
        campo_quantidade.value = texto
        page.update()

    def formatar_validade(e):
        texto = "".join(filter(str.isdigit, e.control.value))
        texto = texto[:8]
        
        formatado = ""

        if len(texto) > 0:
            formatado += texto[:2]
        if len(texto) > 2:
            formatado += "/" + texto[2:4]
        if len(texto) > 4:
            formatado += "/" + texto[4:8]

        campo_validade.value = formatado
        page.update()








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
    layout = ft.Container(
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

    return layout
    