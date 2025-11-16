import flet as ft


def main(page: ft.Page):
    codigo = ft.TextField(label= "Código:", width=610, bgcolor=ft.Colors.WHITE)
    nome = ft.TextField(label= "Nome do Produto:", width=610, bgcolor=ft.Colors.WHITE) 
    preco_custo = ft.TextField(label= "Preço de Custo:", bgcolor=ft.Colors.WHITE, width=610)
    preco_venda = ft.TextField(label= "Preço de venda:", bgcolor=ft.Colors.WHITE, width=610, read_only=True)

    layout = ft.AlertDialog()

    page.add(layout)


ft.app(target=main)
