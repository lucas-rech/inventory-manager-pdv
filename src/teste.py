import flet as ft


def main(page: ft.Page):
    codigo = ft.TextField(label= "Código:", width=610, bgcolor=ft.Colors.WHITE)
    nome = ft.TextField(label= "Nome do Produto:", width=610, bgcolor=ft.Colors.WHITE) 
    preco_custo = ft.TextField(label= "Preço de Custo:", bgcolor=ft.Colors.WHITE, width=610)
    preco_venda = ft.TextField(label= "Preço de venda:", bgcolor=ft.Colors.WHITE, width=610, read_only=True)

    layout = ft.Container(
        content=ft.Column(
            controls=[
                ft.ResponsiveRow(
                    controls=[
                        ft.Container(
                            content=codigo,
                            col={"xs": 12, "sm": 6, "md":3},
                        ),
                        ft.Container(
                            content=nome,
                            col={"xs": 12, "sm": 6, "md":3},
                        ),
                    ],

                    alignment=ft.MainAxisAlignment.CENTER,
                ),

                ft.ResponsiveRow(
                    controls=[
                        ft.Container(
                            content=preco_custo,
                            col={"xs": 12, "sm": 6, "md":3},
                        ),

                        ft.Container(
                            content=preco_venda,
                            col={"xs": 12, "sm": 6, "md":3},
                        ),
                    ],

                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            ],

            alignment=ft.MainAxisAlignment.CENTER,
        ),

        expand=True
    )

    page.add(layout)


ft.app(target=main)
