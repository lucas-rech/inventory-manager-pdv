import flet as ft
# Botão adicionar produtos: 
def botao_adicionar(action):
    return ft.ElevatedButton(
        text= "Adicionar",
        bgcolor= "#507656",
        color= ft.Colors.WHITE,
        on_click=action,
        height=50,
        width=110,
    ) 