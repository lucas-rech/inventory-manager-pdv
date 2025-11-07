import flet as ft

def main(page: ft.Page):

    # TextField que ficará DENTRO do modal
    campo_valor = ft.TextField(label="Digite algo", width=100)
    campo_nome = ft.TextField(label="Digite o nome", width=100)
    campo3 = ft.TextField(label="Digite o nome", width=100)
    campo4 = ft.TextField(label="Digite o nome", width=100)

    # Funções de controle
    def abrir_modal(e):
        page.open(dlg)
        page.update()

    def fechar_modal(e=None):
        page.close(dlg)
        page.update()

    def confirmar(e):
        print("Valor digitado:", campo_valor.value)
        fechar_modal()

    # Definição do modal
    dlg = ft.AlertDialog(
        content=ft.Container(
            ft.Column(
                [
                    ft.Row([campo_valor, campo_nome], alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row([campo3, campo4], alignment=ft.MainAxisAlignment.CENTER),
                ], 
            ),
            width=500,
            height=400,
        ),

        modal=True,
        title=ft.Text("Adicionar informação"),
        actions=[
            ft.TextButton("Cancelar", on_click=fechar_modal),
            ft.ElevatedButton("Confirmar", on_click=confirmar),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    # Botão que abre o modal
    page.add(
        ft.ElevatedButton("Abrir modal", on_click=abrir_modal)
    )

ft.app(target=main)
