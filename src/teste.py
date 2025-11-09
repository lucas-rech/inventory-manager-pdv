import flet as ft

def main(page: ft.Page):
    imagem = ft.Image(src="src/assets/pagamento-cartao.jpg")

    # Funções de controle
    def abrir_modal(e):
        page.open(dlg)
        page.update()

    def fechar_modal(e=None):
        page.close(dlg)
        page.update()

    def confirmar(e):
        print("Valor digitado:")
        fechar_modal()

    # Definição do modal
    dlg = ft.AlertDialog(
        content=ft.Container(
            ft.Column(
                [
                    ft.Row([imagem], alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row([ft.Text("Aproxime ou insira o cartão na maquininha", size=20)], alignment=ft.MainAxisAlignment.CENTER)
                ], 
                alignment=ft.MainAxisAlignment.CENTER,
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
        bgcolor=ft.Colors.WHITE,
    )

    # Botão que abre o modal
    page.add(
        ft.ElevatedButton("Abrir modal", on_click=abrir_modal)
    )

ft.app(target=main)
