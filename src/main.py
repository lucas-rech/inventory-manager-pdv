import flet as ft

from ui.pages.tela_login_usuario import criar_tela_login
from ui.components.conteudo.header import criar_header
from ui.components.conteudo.menu_lateral import criar_menu_lateral
from ui.components.botoes.escolha_de_cadastro import criar_botoes_cadastro
from ui.pages.tela_cadastro_produto import cadastrar_produtos
from ui.pages.tela_estoque import criar_tela_estoque
from ui.pages.tela_cadastro_cliente import cadastrar_clientes
from ui.pages.tela_clientes import criar_tela_clientes
from ui.pages.tela_pdv import criar_tela_pdv

def main(page: ft.Page):
    page.title = "Sistema Mercado"
    page.bgcolor = "#E8E3DE"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.horizontal_alignment = "center"
    page.window.maximized = True
    page.window.resizable = True


    # Função para trocar para a tela de cadastro de produtos:
    def informacoes_produto(e):
        conteudo_completo.controls.clear() # Limpa toda a tela (menos o menu lateral).
        header.content.value = "Cadastrar Produtos"
        conteudo_completo.controls.append(header) # Adiciona o cabeçalho à tela.
        conteudo_completo.controls.append(tela_produto) # Adiciona os campos de informações do produto à tela.

        page.update()

    def informacoes_cliente(e):
        conteudo_completo.controls.clear()
        header.content.value = "Cadastrar Clientes"
        conteudo_completo.controls.append(header)
        conteudo_completo.controls.append(tela_cliente)

        page.update()


    # Lista de produtos que armazenará os produtos adicionados ao estoque:
    produtos = []

    # Lista de clientes que armazenará os clientes cadastrados:
    clientes = []

    # Lista com o resumo da compra:
    resumo_compra = []

    # Layout inicial completo: (Começa vazio)
    conteudo_completo = ft.Column(expand=True)

    # Cabeçalho:
    header = criar_header("Venda")

    # Tela Cadastro de Produtos
    tela_produto = cadastrar_produtos(page, produtos, conteudo_completo, header)

    # Tela Cadastro de Clientes:
    tela_cliente = cadastrar_clientes(page, clientes, conteudo_completo, header)

    # Método do login no sistema
    def entrar():
        page.clean()
        page.update()
        page.add(layout)

    # Tela Login:
    tela_login = criar_tela_login(page, entrar)
    page.add(tela_login)
    
    # Tela onde será feita a venda:
    tela_pdv = criar_tela_pdv(resumo_compra, produtos, page, header, conteudo_completo)

    # Aqui sim adicionamos o conteúdo inicial:
    conteudo_completo.controls.extend([header, tela_pdv])


    # Navegação do menu lateral:
    def selecionar_menu(e):
            index = e.control.selected_index # captura o index selecionado no rail (o rail cria uma "lista" de opções para navegação)

            if index == 0:
                conteudo_completo.controls.clear()
                header.content.value = "Venda"
                conteudo_completo.controls.append(header)
                conteudo_completo.controls.append(tela_pdv)

            elif index == 1:
                conteudo_completo.controls.clear()
                header.content.value = "Escolha o tipo de cadastro"
                conteudo_completo.controls.append(header)
                conteudo_completo.controls.append(criar_botoes_cadastro(informacoes_produto, informacoes_cliente))

            elif index == 2:
                conteudo_completo.controls.clear()
                header.content.value = "Estoque"
                conteudo_completo.controls.append(header)
                conteudo_completo.controls.append(criar_tela_estoque(produtos, page))

            elif index == 3:
                conteudo_completo.controls.clear()
                header.content.value = "Clientes"
                conteudo_completo.controls.append(header)
                conteudo_completo.controls.append(criar_tela_clientes(clientes, page))

            page.update()

    # Menu lateral:
    rail = criar_menu_lateral(selecionar_menu)

    # 
    layout = ft.Row(
        [
            rail,
            conteudo_completo 
        ],

        expand=True
    )

ft.app(target=main)
