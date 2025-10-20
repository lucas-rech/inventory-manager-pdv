import flet as ft
from ui.components.botoes.botao_finalizar import criar_botao_finalizar

def criar_tela_finalizar_compra(area_tabela, texto_total): # Aqui será inserido a tabela com o resumo da compra, já formatada.

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
                    ft.Column([menu_forma_pagamento, botao_finalizar], alignment=ft.MainAxisAlignment.START),
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