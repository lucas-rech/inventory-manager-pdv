import flet as ft
import time
from ui.components.botoes.botao_adicionar import criar_botao_adicionar
from ui.components.botoes.botao_finalizar import criar_botao_finalizar

def criar_tela_pdv(resumo_compra, produtos, page, header, conteudo_completo):
    # Função que permitirá apenas números no campo de código:
    def formatar_codigo(e):
        texto = "".join(filter(str.isdigit, e.control.value)) # Apenas junte a string do que está sendo digitado o que for número.
        codigo.value = texto # Atualiza o campo enquanto o usuário digita.
        page.update() # Atualiza a tela


    codigo = ft.TextField(label="Código:", width=630, bgcolor=ft.Colors.WHITE, border=ft.border.all(1, color="#765070"), on_change=formatar_codigo)

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

    # Função que irá formatar o preco de venda para float novamente sem a formatação contábil para que não dê TypeError, já que o preco_venda está armazenado como string na lista de produtos:
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

    tela_finalizar_compra = criar_tela_finalizar_compra(area_tabela, texto_total, page) # Cirando a tela de finalizar compra
    
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

def criar_tela_finalizar_compra(area_tabela, texto_total, page): # Aqui será inserido a tabela com o resumo da compra, já formatada.

    # Estou fazendo uma cópia do campo de total para evitar conflitos.
    novo_total_compra = ft.Container(
        content=texto_total,
        bgcolor="#85A289",
        padding=ft.padding.all(15),
        border_radius=13,
        alignment=ft.alignment.center,
        width=750,
        height=100,
    )

    qr_code = ft.Image(src="src/assets/qr-code.png", width=200, height=200, visible=False)

    # escolha conforme o método de pagamento
    def escolha_pagamento(e):
        if e.control.value == "pix":
            qr_code.visible = True
            page.update()
            time.sleep(3)
            qr_code.visible = False
            page.update()

        if e.control.value == "dinheiro":
            pass
        if e.control.value == "débito":
            pass
        if e.control.value == "crédito":
            pass

    # Menu de seleção da forma de pagamento:
    menu_forma_pagamento = ft.Container(
        ft.RadioGroup(
            content=ft.Column(
                [
                    ft.Radio(label="💠 Pix", value="pix"), # O value será util para capturar a forma de pagamento selecionada, para que possa ser utilizada posteriormente.
                    ft.Radio(label="💵 Dinheiro", value="dinheiro"),
                    ft.Radio(label="💳 Débito", value="débito"),
                    ft.Radio(label="💳 Crédito", value="crédito"),
                ],
                spacing=10,
            ),
            on_change=escolha_pagamento,
            value=None, # O valor inicial é nulo, nenhuma opção selecionada
        ),

        width=250,
        height=180,
        border=ft.border.all(1, "#765070"),
        border_radius=10,
    )





    botao_finalizar = criar_botao_finalizar(True)
    botao_finalizar.width = 250

    layout = ft.Container(
        ft.Row(
            [
                ft.Column([area_tabela, novo_total_compra], alignment=ft.MainAxisAlignment.START),
                ft.Column([menu_forma_pagamento, botao_finalizar, qr_code], alignment=ft.MainAxisAlignment.START),
            ],

            spacing=10,
            alignment=ft.MainAxisAlignment.CENTER,
        ),

        bgcolor=ft.Colors.WHITE,
        expand=True,
        padding=20,
        border_radius=13,
    )

    return layout