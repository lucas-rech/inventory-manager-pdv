import flet as ft
from ui.components.botoes.botao_adicionar import criar_botao_adicionar

def criar_tela_pdv(resumo_compra, produtos, page):
    codigo = ft.TextField(label="Código:", width=630, bgcolor=ft.Colors.WHITE, border=ft.border.all(1, color="#765070"))

    tabela_resumo_venda = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Código", weight="bold")),
            ft.DataColumn(ft.Text("Produto", weight="bold")),
            ft.DataColumn(ft.Text("Preço", weight="bold")),
            ft.DataColumn(ft.Text("Quantidade", weight="bold")),
            ft.DataColumn(ft.Text("Subtotal", weight="bold")),
        ],
        rows=[],
    )

    def get_informacoes_produto(codigo):
        for c in produtos:
            if c["codigo"] == codigo:
                return {
                    "codigo": c["codigo"],
                    "nome": c["nome"],
                    "preco_venda": float(c["preco_venda"]),
                    "quantidade": 1,
                }
        return None

    total = 0
    texto_total = ft.Text(value=f"Total: R$ {total:.2f}", weight="bold", size=40)

    def atualizar(e):
        nonlocal total
        produto_encontrado = get_informacoes_produto(codigo.value)
        if not produto_encontrado:
            return

        resumo_compra.append(produto_encontrado)
        tabela_resumo_venda.rows.clear()
        total = 0

        for p in resumo_compra:
            subtotal = p["preco_venda"] * p["quantidade"]
            total += subtotal
            tabela_resumo_venda.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(value=p["codigo"])),
                        ft.DataCell(ft.Text(p["nome"])),
                        ft.DataCell(ft.Text(p["preco_venda"])),
                        ft.DataCell(ft.Text(p["quantidade"])),
                        ft.DataCell(ft.Text(f"{subtotal:.2f}")),
                    ],
                )
            )

        texto_total.value = f"Total: R$ {total:.2f}"
        codigo.value = ""
        codigo.focus()
        page.update()

    botao = criar_botao_adicionar(atualizar)

    # 🔹 Área da tabela limitada (com scroll)
    area_tabela = ft.Container(
        content=ft.Column(
            [
                ft.Text("Resumo da Compra", size=24, weight="bold"),
                tabela_resumo_venda
            ],
            spacing=20,
            height=400,
            scroll=ft.ScrollMode.AUTO,
        ),
        width=750,  # Define o tamanho máximo da tabela
        padding=20,
        border=ft.border.all(1, color="#765070"),
        border_radius=10,
    )

    # 🔹 Campo total fixo
    total_compra = ft.Container(
        content=texto_total,
        bgcolor="#85A289",
        padding=ft.padding.all(15),
        border_radius=13,
        alignment=ft.alignment.center_right,
        width=400,
        height=100,
    )

    # 🔹 Layout principal com Stack (mantém o total fixo)
    layout = ft.Container(
            ft.Stack(
            controls=[
                ft.Row(
                    [
                        ft.Column(
                            [
                                ft.Row([codigo, botao]),
                                area_tabela,  # à esquerda
                            ]
                        ),

                        ft.Image(src="src/assets/LogoSombreado.png", expand=True)  
                    ],
                    expand=True,
                ),
                ft.Container(
                    content=total_compra,
                    right=30,   # canto inferior direito
                    bottom=30,
                ),
            ],
            expand=True,
        ),

        expand=True, 
        bgcolor=ft.Colors.WHITE,
        padding=20,
        border_radius=13,
    )

    return layout
