import flet as ft

def criar_botao_finalizar(action):
    return ft.ElevatedButton(
        content= ft.Text("Finalizar Compra", size=16),
        bgcolor= "#507656",
        color= ft.Colors.WHITE,
        on_click=action,
        height=50,
        width=200,
    ) 
