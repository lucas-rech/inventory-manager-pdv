import flet as ft
from ui.components.botoes.botao_adicionar import criar_botao_adicionar
from ui.pages.tela_finalizar_compra import criar_tela_finalizar_compra
from ui.components.botoes.botao_finalizar import criar_botao_finalizar

def criar_tela_pdv(resumo_compra, produtos, page, header, conteudo_completo):
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

    # Função que irá formatar o preco de venda para float novamente sem a formatação contábil:
    def formatar_preco_venda(pvenda):
        valor_pvenda = pvenda.replace("R$", "").replace(".", "").replace(",", ".") # Retira o cifrão e muda as vírgulas para o padrão de pontos.
        return valor_pvenda # Retorna o valor bruto, sem formatação nenhuma.

    def get_informacoes_produto(codigo):
        for c in produtos:
            if c["codigo"] == codigo:
                formatar_preco_venda(c["preco_venda"])
                return {
                    "codigo": c["codigo"],
                    "nome": c["nome"],
                    "preco_venda": float(formatar_preco_venda(c["preco_venda"])),
                    "quantidade": 1,
                }
        return None

    total = 0
    texto_total = ft.Text(value=f"Total: R$ {total:.2f}", weight="bold", size=40)

    def atualizar(e):
        nonlocal total # nonlocal se refere ao total decarado acima
        produto_encontrado = get_informacoes_produto(codigo.value)
        if not produto_encontrado: # Se não encontrar o produto não retorna nada e para a função aqui.
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

    botao_adicionar = criar_botao_adicionar(atualizar)

    # 🔹 Área da tabela limitada (com scroll)
    area_tabela = ft.Container(
        content=ft.Column(
            [
                ft.Text("Resumo da Compra", size=24, weight="bold"),
                tabela_resumo_venda
            ],
            spacing=20,
            scroll=ft.ScrollMode.AUTO,
        ),
        width=750,  # Define o tamanho máximo da tabela
        expand=True,
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

    tela_finalizar_compra = criar_tela_finalizar_compra(area_tabela, texto_total) # Cirando a tela de finalizar compra
    
    def finalizar_compra(e): # Atualização do conteúdo para a tela de finaizar compra
        conteudo_completo.controls.clear() # Limpa tudo
        header.content.value = "Finalizar Compra" # Atualiza o header
        conteudo_completo.controls.append(header) # Adiciona ele na página
        conteudo_completo.controls.append(tela_finalizar_compra) # Adiciona a tela de finaliar compra

        page.update() # Atualiza a página para mostrar as alterações

    botao_finalizar_compra = criar_botao_finalizar(finalizar_compra)

    # 🔹 Layout principal com Stack (mantém o total fixo)
    layout = ft.Container(
            ft.Stack(
            controls=[
                ft.Row(
                    [
                        ft.Column(
                            [
                                ft.Row([codigo, botao_adicionar]),
                                area_tabela,  # à esquerda
                                ft.Row([botao_finalizar_compra], width=750, alignment=ft.MainAxisAlignment.END),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
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
