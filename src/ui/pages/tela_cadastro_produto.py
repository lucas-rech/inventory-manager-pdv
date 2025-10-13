from flet import *
from ui.components.botoes.botao_adicionar import botao_adicionar

# Função que criará a tela de cadastro de produto
def cadastrar_produtos(page, produtos):
    # Campos do formulário:
    codigo = TextField(label= "Código:", width=610, bgcolor=Colors.WHITE)
    nome = TextField(label= "Nome do Produto:", width=610, bgcolor=Colors.WHITE) 
    preco_custo = TextField(label= "Preço de Custo:", bgcolor=Colors.WHITE, width=610)
    preco_venda = TextField(label= "Preço de venda:", bgcolor=Colors.WHITE, width=610)
    quantidade = TextField(label= "Quantidade:", bgcolor=Colors.WHITE, width=610)
    validade = TextField(label= "Validade:", bgcolor=Colors.WHITE, width=610)

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


    botao = botao_adicionar(adicionar_produto)

    # Tela onde serão inseridas as informações dos produtos:
    tela_informacoes_produto = Container(
        Column(
            [
                Row([codigo, nome], alignment=MainAxisAlignment.CENTER),
                Row([preco_custo, preco_venda], alignment=MainAxisAlignment.CENTER),
                Row([quantidade, validade], alignment=MainAxisAlignment.CENTER),

                Container(botao, alignment=alignment.center),
            ],

            alignment=MainAxisAlignment.CENTER,
        ),

        expand=True
    )

    return tela_informacoes_produto
