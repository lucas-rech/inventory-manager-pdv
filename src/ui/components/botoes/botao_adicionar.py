import flet as ft
# Botão adicionar produtos: 
def criar_botao_adicionar(action):
    layout_botao = ft.ElevatedButton(
        content= ft.Text("Adicionar", size=16),
        bgcolor= "#507656",
        color= ft.Colors.WHITE,
        on_click=action,
        height=50,
        width=110,
    ) 

    return ft.Container(
        content=layout_botao,
        col={"xs": 12, "sm": 4, "md": 3, "lg": 2}
    )