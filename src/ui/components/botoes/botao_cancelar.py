import flet as ft
import asyncio

# Função que criará o botão de cancelar: 
def criar_botao_cancelar(action, page):
    confirmado = False  # flag que indica se o usuário já confirmou

    # Função executada quando o usuário confirma (clica novamente durante a contagem)
    def acao_confirmada(e):
        nonlocal confirmado # permite alterar a variável 'confirmado' que está no escopo externo.
        confirmado = True # marca que o usuário confirmou.

        layout_botao.content.value = "Cancelar" # volta o texto do botão para "Cancelar"
        layout_botao.on_click = lambda e: page.run_task(confirmar_acao, e) # redefine o clique para iniciar a contagem novamente quando clicado no futuro. (Se você passar direto confirmar_acao, vai dar erro do tipo AssertionError)

        page.update() # atualiza a UI para refletir as mudanças
        action(e) # executa a ação externa passada (voltar_para_escolha)

    # Define uma função assíncrona. Para podermos usar await (parecido com o sleep) dentro dela.
    async def confirmar_acao(e):
        nonlocal confirmado # permite alterar 'confirmado' dentro desta função
        confirmado = False # recomeça com confirmado = False (antes do usuário confirmar)
        layout_botao.on_click = acao_confirmada # durante a contagem, o próximo clique chama acao_confirmada
        
        # loop de contagem regressiva (10, 9, ..., 1)
        for i in range(10, 0, -1):
            if confirmado: # se o usuário clicou para confirmar, interrompe a contagem.
                break

            layout_botao.content.value = f"Confirma? ({i})"  # atualiza o texto para mostrar a contagem.
            page.update() # atualiza a tela para mostrar o novo texto.
            await asyncio.sleep(1) # pausa 1 segundo sem travar a interface. (se fosse com o sleep, até que o loop não terminasse, a tela permaneceria "congelada".)

        # quando a contagem termina (ou foi interrompida), volta ao estado inicial
        layout_botao.content.value = "Cancelar" # O texto do botão volta para "Cancelar"
        layout_botao.on_click = lambda e: page.run_task(confirmar_acao, e) # A função que ele executará a ser clicado volta a ser confirmar_acao. (Se você passar direto confirmar_acao, vai dar erro do tipo AssertionError)
        page.update() # atualiza a tela

    layout_botao = ft.ElevatedButton(
        bgcolor="#9B3E3E", 
        content=ft.Text("Cancelar", size=16),
        color=ft.Colors.WHITE,
        on_click=lambda e: page.run_task(confirmar_acao, e), # ao clicar, inicia a contagem sem travar a UI. (Se você passar direto confirmar_acao, vai dar erro do tipo AssertionError)
        height=50,
        width=125,
    )

    return ft.Container(
        content=layout_botao,
        col={"xs": 12, "sm": 4, "md": 3, "lg": 1.4}
    )