import flet as ft
# Botão adicionar produtos: 
def botao_adcionar(action):
    return ft.ElevatedButton(
        text= "Adicionar",
        bgcolor= ft.Colors.BLUE_900,
        color= ft.Colors.WHITE,
        on_click=action,
        height=50,
        width=110,
    ) 