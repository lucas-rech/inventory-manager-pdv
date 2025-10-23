import flet as ft

def criar_botoes_cadastro(acao_produtos, acao_clientes):

    # Botão para cadastrar clientes:
    clientes = ft.Container(
        content= ft.Text("Clientes", color="#e8e3de", style=ft.TextStyle(weight=ft.FontWeight.BOLD), size=23),
        bgcolor= "#765070",
        width= 200,
        height= 150,
        alignment= ft.alignment.center,
        border_radius=8,
        ink=True, # Atribui um efeito de click
        on_click=acao_clientes, # Atribui a função de click para um container (True apenas ativa a função de click sem nenhuma função). Aqui será chamada a função informacoes_cliente que está definida na main.
    )

    # Botão para cadastrar produtos:
    produtos = ft.Container(
        content= ft.Text("Produtos", color="#e8e3de", style=ft.TextStyle(weight=ft.FontWeight.BOLD), size=23),
        bgcolor= "#765070",
        width= 200,
        height= 150,
        alignment= ft.alignment.center,
        border_radius=8,
        ink=True, # Atribui um efeito de click
        on_click=acao_produtos, # Atribui a função de click para um container (True apenas ativa a função de click sem nenhuma função). Aqui será chamada a função informacoes_produto que está definida na main.
    )

    # Juntando os dois botões em um container só:
    return ft.Container(
        ft.Row([clientes, produtos], alignment=ft.MainAxisAlignment.CENTER),
        alignment=ft.alignment.center,   
        expand=True
    )
