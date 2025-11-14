import flet as ft

def criar_botoes_cadastro(acao_produtos, acao_clientes, acao_usuarios):

    # Botão para cadastrar clientes:
    clientes = ft.Container(
        content=ft.Column(
            [   
                ft.Icon(ft.Icons.PERSON, size=65, weight="bold",color="#e8e3de"), 
                ft.Text("Clientes", size=23, weight="bold", color="#e8e3de", style=ft.TextStyle(weight=ft.FontWeight.BOLD)),
                              
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=5
        ),

        col={"xs":12, "sm":6, "md":4, "lg":2},
        width=200,
        height=150,
        bgcolor="#765070",
        border_radius=8,
        alignment=ft.alignment.center,
        ink=True,  # efeito de clique visual
        on_click=acao_clientes
    )

    # Botão para cadastrar produtos:
    produtos = ft.Container(
        content= ft.Column(
            [
                ft.Icon(ft.Icons.INVENTORY_2, size = 60, weight="bold",color="#e8e3de"),
                ft.Text("Produtos", size=23, weight="bold", color="#e8e3de", style=ft.TextStyle(weight=ft.FontWeight.BOLD)),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=5
        ),

        col={"xs":12, "sm":6, "md":4, "lg":2},
        bgcolor= "#765070",
        width= 200,
        height= 150,
        alignment= ft.alignment.center,
        border_radius=8,
        ink=True, # Atribui um efeito de click
        on_click=acao_produtos, # Atribui a função de click para um container (True apenas ativa a função de click sem nenhuma função). Aqui será chamada a função informacoes_produto que está definida na main.
    )

    # Botão para cadastrar produtos:
    usuarios = ft.Container(
        content= ft.Column(
            [
                ft.Icon(ft.Icons.PERSON_ADD_ALT_SHARP, size = 65, weight="bold",color="#e8e3de"),
                ft.Text("Usuarios", size=23, weight="bold", color="#e8e3de", style=ft.TextStyle(weight=ft.FontWeight.BOLD)),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=5
        ),

        col={"xs":12, "sm":6, "md":4, "lg":2},
        bgcolor= "#765070",
        width= 200,
        height= 150,
        alignment= ft.alignment.center,
        border_radius=8,
        ink=True, # Atribui um efeito de click
        on_click=acao_usuarios, # Atribui a função de click para um container (True apenas ativa a função de click sem nenhuma função). Aqui será chamada a função informacoes_produto que está definida na main.
    )

    # Juntando os dois botões em um container só:
    return ft.Container(
        content=ft.ResponsiveRow(
            controls=[clientes, produtos, usuarios], alignment=ft.MainAxisAlignment.CENTER,
        ),

        alignment=ft.alignment.center,   
        expand=True
    )
