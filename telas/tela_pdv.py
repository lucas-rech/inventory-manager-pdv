import flet as ft

# Tela que será mostrada ao selecionar venda no menu lateral:
def criar_tela_pdv():
    layout = ft.Container(
        expand=True,
        bgcolor=ft.Colors.WHITE,
        margin=0,
        border_radius=15
    )

    return layout