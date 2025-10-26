import flet as ft
# Botão adicionar produtos: 
def criar_botao_adicionar(action):
    return ft.ElevatedButton(
        content= ft.Text("Adicionar", size=16),
        bgcolor= "#507656",
        color= ft.Colors.WHITE,
        on_click=action,
        height=50,
        width=110,
    ) 