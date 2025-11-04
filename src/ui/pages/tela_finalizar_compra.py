import flet as ft
import subprocess
import sys # bibliotecas para criar uma nova janela
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

    def abrir_nova_janela(e):
                
        # Cria um script temporário para a nova janela, importante pois tem outras bibliotecas dentro dele
        script = f"""
import flet as ft
import time
import threading
import screeninfo


def nova_janela(page: ft.Page):
    page.title = "Nova janela"
    # Define o tamanho da janela
    page.window.width = 500
    page.window.height = 500
    screen = screeninfo.get_monitors()[0]


    page.window.left = (screen.width - page.window.width) // 2
    page.window.top = (screen.height - page.window.height) // 2

    
    page.add(
        ft.Container(
            alignment=ft.alignment.center,
            content=ft.Image(
                src="src/assets/qr-code.png",
                )
            )
        )
    
    # Função para fechar a janela após o tempo definido
    def fechar_apos_tempo():
        time.sleep(3)
        page.window.close()
    
    # Inicia o fechamento automático em uma thread separada
    thread = threading.Thread(target=fechar_apos_tempo, daemon=True)
    thread.start()

ft.app(target=nova_janela)
"""
        # Executa o script em um novo processo Python
        subprocess.Popen([sys.executable, "-c", script])

    # escolha conforme o método de pagamento
    def escolha_pagamento(e):
        if e.control.value == "pix":
            abrir_nova_janela(e)

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