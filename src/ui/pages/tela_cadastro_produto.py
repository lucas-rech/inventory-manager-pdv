import flet as ft
from ui.components.botoes.botao_adicionar import criar_botao_adicionar
from ui.components.botoes.botao_cancelar import criar_botao_cancelar


# Função que criará a tela de cadastro de produto
def cadastrar_produtos(page, produtos):
    # Campos do formulário:
    codigo = ft.TextField(label= "Código:", width=610, bgcolor=ft.Colors.WHITE)
    nome = ft.TextField(label= "Nome do Produto:", width=610, bgcolor=ft.Colors.WHITE) 
    preco_custo = ft.TextField(label= "Preço de Custo:", bgcolor=ft.Colors.WHITE, width=610)
    preco_venda = ft.TextField(label= "Preço de venda:", bgcolor=ft.Colors.WHITE, width=610)
    quantidade = ft.TextField(label= "Quantidade:", bgcolor=ft.Colors.WHITE, width=610)
    validade = ft.TextField(label= "Validade:", bgcolor=ft.Colors.WHITE, width=610)

    # Função que adicionará os items ao estoque:
    def adicionar_produto(e):
        novo_produto = { # Adiciona os valores digitados em cada campo às respectivas chaves no dicionário.
            "codigo":codigo.value,
            "nome":nome.value,
            "preco_custo":preco_custo.value,
            "preco_venda":preco_venda.value,
            "quantidade":quantidade.value,
            "validade":validade.value
        }

        produtos.append(novo_produto) # Adiciona todas as informações do produto à lista "produtos".

        for campo in [codigo, nome, preco_custo, preco_venda, quantidade, validade]:
            campo.value = "" # Limpa todos os campos, substituindo o que foi digitado por uma string vazia ("").

        page.update() # Atualiza a página para mostrar o que foi alterado.


    botao_adicionar = criar_botao_adicionar(adicionar_produto)
    botao_cancelar = criar_botao_cancelar(True)

    # Tela onde serão inseridas as informações dos produtos:
    tela_informacoes_produto = ft.Container(
        ft.Column(
            [
                ft.Row([codigo, nome], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([preco_custo, preco_venda], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([quantidade, validade], alignment=ft.MainAxisAlignment.CENTER),

                ft.Row([botao_adicionar, botao_cancelar], alignment=ft.MainAxisAlignment.CENTER),
            ],

            alignment=ft.MainAxisAlignment.CENTER,
        ),

        expand=True,
        bgcolor=ft.Colors.WHITE,
        margin=0,
        border_radius=15,
    )

    return tela_informacoes_produto
