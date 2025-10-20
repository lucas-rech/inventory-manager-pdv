import flet as ft

# Função que criará o botão de cancelar: 
def criar_botao_cancelar(action):
    return ft.ElevatedButton(
        bgcolor="#9B3E3E",
        text= "Cancelar",
        color= ft.Colors.WHITE,
        on_click=action, # Ação que será atribuída a ele.
        height=50,
        width=110,
    )