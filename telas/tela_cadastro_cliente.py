import flet as ft
from botoes.botao_adicionar import botao_adcionar

def cadastrar_clientes(page, clientes):
    # Campos do formulário para o cadastro de um cliente:
    nome = ft.TextField(label="Nome do cliente", bgcolor=ft.Colors.WHITE, width=610)

    numero = ft.TextField(label="Número de telefone do cliente", hint_text="Ex: (XX) XXXX-XXXX", bgcolor=ft.Colors.WHITE, width=610)

    def adicionar_cliente(e):
        novo_cliente = {
            "nome":nome.value,
            "numero":numero.value,
        }

        clientes.append(novo_cliente)
        print(clientes)

        for campo in [nome, numero]:
            campo.value = ""

        page.update()

    botao = botao_adcionar(adicionar_cliente)

    layout = ft.Container(
        ft.Column(
            [
                ft.Row([nome], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([numero], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([botao], alignment=ft.MainAxisAlignment.CENTER)
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ), 

        expand=True,
        bgcolor=ft.Colors.WHITE,
        margin=0,
        border_radius=15,
    )

    return layout
