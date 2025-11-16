import flet as ft
import datetime


def main(page: ft.Page):
    def abrir_datepicker(e):
        # Abre o DatePicker quando clicar no botão ou no campo
        page.open(date_picker)


    codigo = ft.TextField(label= "Código:", width=610, bgcolor=ft.Colors.WHITE)
    nome = ft.TextField(label= "Nome do Produto:", width=610, bgcolor=ft.Colors.WHITE) 
    preco_custo = ft.TextField(label= "Preço de Custo:", bgcolor=ft.Colors.WHITE, width=610)
    preco_venda = ft.TextField(label= "Preço de venda:", bgcolor=ft.Colors.WHITE, width=610, read_only=True)
    quantidade = ft.TextField(label= "Quantidade:", bgcolor=ft.Colors.WHITE, width=610)
    validade = ft.TextField(label= "Validade:", bgcolor=ft.Colors.WHITE, width=560)
    selecionar_data = ft.IconButton(icon=ft.Icons.CALENDAR_MONTH, on_click=abrir_datepicker, icon_color=ft.Colors.BLACK)

    # essas linhas padronizam formatos da página em português (especialmente datepicker)
    page.locale_configuration = ft.LocaleConfiguration(
        supported_locales=[ft.Locale(language_code="pt", country_code="BR")],
        current_locale=ft.Locale(language_code="pt", country_code="BR")
    )

    def handle_change(e):
        # Atualiza o TextField com a data selecionada formatada
        data_formatada = e.control.value.strftime('%d/%m/%Y')
        validade.value = data_formatada
        validade.update()
        page.close(date_picker)

    def handle_dismissal(e):
        # Ação quando o DatePicker é fechado sem selecionar
        page.close(date_picker)

    # Cria o DatePicker com as configurações
    date_picker = ft.DatePicker(
        first_date=datetime.datetime(year=2025, month=1, day=1),
        last_date=datetime.datetime.today() + datetime.timedelta(90),
        on_change=handle_change,
        on_dismiss=handle_dismissal,
    )

    editar = ft.AlertDialog(
        content=ft.Container(
            content=ft.Column(
                controls=[
                    ft.ResponsiveRow(
                        controls=[
                            ft.Container(
                                content=ft.Text("Editar Dados", size=20, weight="bold"),
                                alignment=ft.alignment.center,
                            )
                        ]
                    ),

                    ft.ResponsiveRow(
                        controls=[
                            ft.Container(
                                content=codigo,
                                col={"xs": 12, "sm":9, "md":6, "lg":6},
                            ),

                            ft.Container(
                                content=nome,
                                col={"xs": 12, "sm":9, "md":6, "lg":6},
                            ),
                        ],

                        alignment=ft.MainAxisAlignment.CENTER,
                    ),

                    ft.ResponsiveRow(
                        controls=[
                            ft.Container(
                                content=quantidade,
                                col={"xs": 12, "sm":9, "md":6, "lg":6},
                            ),
                            
                            ft.Container(
                                content=validade,
                                col={"xs": 10, "sm":8, "md":5, "lg":4.5},
                            ),

                            ft.Container(
                                content=selecionar_data,
                                col={"xs": 2, "sm":1, "md":1, "lg":1.5},
                            ),
                        ],

                        alignment=ft.MainAxisAlignment.CENTER,
                    ),

                    ft.ResponsiveRow(
                        controls=[
                            ft.Container(
                                content=preco_custo,
                                col={"xs": 12, "sm":9, "md":6, "lg":6},
                            ),
                            
                            ft.Container(
                                content=preco_venda,
                                col={"xs": 12, "sm":9, "md":6, "lg":6},
                            ),
                        ],

                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                ],

                alignment=ft.MainAxisAlignment.CENTER,
                spacing=10,
            ),

            width=530,
            height=400,
        ),

        alignment=ft.alignment.center,
    )

    def abrir_editar(e):
        page.open(editar)
        page.update()

    botao_editar = ft.IconButton(icon=ft.Icons.EDIT, on_click=abrir_editar)

    page.add(botao_editar)


ft.app(target=main)
