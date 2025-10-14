import flet as ft
from ui.components.botoes.botao_adicionar import botao_adicionar

# Tela que será mostrada ao selecionar venda no menu lateral:
def criar_tela_pdv(resumo_compra, produtos, page):
    codigo = ft.TextField(label="Código:", width=610, bgcolor=ft.Colors.WHITE) # Campo de texto que receberá o código do produto.

    tabela_resumo_venda = ft.DataTable( # Aqui nesta tabela serão adicionados os produtos de uma venda.
        columns= [
            ft.DataColumn(ft.Text("Código")), #Aqui são definidas as colunas e o qual será o título de cada uma. (Dentro de uma DataTable/Tabela, terão 4 colunas com os títulos: Código, Produto, Preço e quantidade, e X linhas que começam em 0 e serão incrementadas conforme forem sendo passados os produtos).
            ft.DataColumn(ft.Text("Produto")),
            ft.DataColumn(ft.Text("Preço")),
            ft.DataColumn(ft.Text("Quantidade")),
        ],

        rows=[]
    )

    # Esta função fará o auto-complete dos dados do produto através do código conseguido no campo "codigo".
    def get_informacoes_produto(codigo): 
        for c in produtos:
            if c["codigo"] == codigo:
                return {
                    "codigo":c["codigo"],
                    "nome":c["nome"],
                    "preco_venda":c["preco_venda"],
                    "quantidade":c["quantidade"],
                }
        return None

    # Essa será a função responsável por atualizar os dados da tabela a cada produto adicionado à compra.
    def atualizar(e):
        produto_encontrado = get_informacoes_produto(codigo.value) # Adiciona a variável produto_encontrado as infonrmações do produto com o mesmo código inserido.

        resumo_compra.append(produto_encontrado)

        print(produto_encontrado)

        tabela_resumo_venda.rows.clear()

        for p in resumo_compra: # Para cada produto na lista com o resumo da compra.
            tabela_resumo_venda.rows.append( # Adicione um alinha à tabela contendo:
                ft.DataRow( # Uma linha de dados com os seguintes valores em cada célula de dados
                    cells=[ 
                        ft.DataCell(ft.Text(p["codigo"])),
                        ft.DataCell(ft.Text(p["nome"])), # Aqui está como nome pois é como está salvo na lista "produtos" que contém os dicionários com cada produto cadastrado, mas preferi utilizar "produtos" na interface.
                        ft.DataCell(ft.Text(p["preco_venda"])),
                        ft.DataCell(ft.Text(p["quantidade"])),
                    ]
                )
            )

        codigo.value = ""
        codigo.focus() # Ativa o auto foco no campo de texto.
        page.update()


    botao = botao_adicionar(atualizar) # Chama a função para que as alterações sejam feitas.

    layout = ft.Container(
        content=ft.Column(
            [
                ft.Row([codigo, botao]),
                ft.Text("Resumo da Compra", size=20, weight="bold"),
                tabela_resumo_venda,
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

    return layout