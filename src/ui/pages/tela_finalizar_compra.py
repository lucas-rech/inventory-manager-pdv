import flet as ft

def criar_tela_finalizar_compra(area_tabela, texto_total): # Aqui será inserido a tabela com o resumo da compra, já formatada.

    # Estou fazendo uma cópia do campo de total para evitar conflitos.
    novo_total_compra = ft.Container(
        content=texto_total,
        bgcolor="#85A289",
        padding=ft.padding.all(15),
        border_radius=13,
        alignment=ft.alignment.center_right,
        width=750,
        height=100,
    )

    layout = ft.Container(
            ft.Row(
                [
                    ft.Column([area_tabela, novo_total_compra]),
                ],
            ),

        bgcolor=ft.Colors.WHITE, 
        expand=True,
        padding=20,
        border_radius=13,
    )

    return layout