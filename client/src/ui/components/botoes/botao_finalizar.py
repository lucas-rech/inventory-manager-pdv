import flet as ft

def criar_botao_finalizar(action, resumo_compra):
    def finalizar(e):
        resumo_compra.clear()
        action(e)

    return ft.ElevatedButton(
        content= ft.Text(value="Finalizar Compra", size=16),
        bgcolor= "#507656",
        color= ft.Colors.WHITE,
        on_click=finalizar,
        height=50,
        width=200,
    ) 
