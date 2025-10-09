from flet import *

def criar_botoes_cadastro(acao_produtos, acao_clientes):

    # Botão para cadastrar clientes:
    clientes = Container(
        content= Text("Clientes", color=Colors.WHITE, style=TextStyle(weight=FontWeight.BOLD), size=23),
        bgcolor= Colors.BLUE_900,
        width= 200,
        height= 150,
        alignment= alignment.center,
        border_radius=8,
        ink=True, # Atribui um efeito de click
        on_click=acao_clientes, # Atribui a função de click para um container (True apenas ativa a função de click sem nenhuma função). Aqui será chamada a função informacoes_cliente que está definida na main.
    )

    # Botão para cadastrar produtos:
    produtos = Container(
        content= Text("Produtos", color=Colors.WHITE, style=TextStyle(weight=FontWeight.BOLD), size=23),
        bgcolor= Colors.BLUE_900,
        width= 200,
        height= 150,
        alignment= alignment.center,
        border_radius=8,
        ink=True, # Atribui um efeito de click
        on_click=acao_produtos, # Atribui a função de click para um container (True apenas ativa a função de click sem nenhuma função). Aqui será chamada a função informacoes_produto que está definida na main.
    )

    # Juntando os dois botões em um container só:
    return Container(
        Column(
            [
                Row([clientes, produtos], alignment=MainAxisAlignment.CENTER),
            ],

            alignment=MainAxisAlignment.CENTER,
        ),
        
        expand=True
    )
