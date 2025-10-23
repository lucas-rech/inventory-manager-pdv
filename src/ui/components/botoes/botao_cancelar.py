import flet as ft
from ui.components.botoes.escolha_de_cadastro import criar_botoes_cadastro

# Função que criará o botão de cancelar: 
def criar_botao_cancelar(action, conteudo_completo, header):
    def cancelar_cadastro(e): # Implementar a volta para a tela de escolha de cadastro!
        pass

    return ft.ElevatedButton(           
        bgcolor="#9B3E3E",
        content=ft.Text("Cancelar", size=16),
        color= ft.Colors.WHITE,
        on_click=action, # Ação que será atribuída a ele.
        height=50,
        width=110,
    )