import flet as ft         # biblioteca Flet para UI
import asyncio            # usado para await asyncio.sleep() (não bloqueia a UI)

def main(page: ft.Page):
    # cria uma função que retorna um botão "Cancelar" que pede confirmação
    # action: função externa a ser executada quando a confirmação ocorrer
    def criar_botao_cancelar(action, page):
        confirmado = False  # flag que indica se o usuário já confirmou

        # Função executada quando o usuário confirma (clica novamente durante a contagem)
        def acao_confirmada(e):
            nonlocal confirmado                     # permite alterar a variável 'confirmado' que está no escopo externo
            confirmado = True                       # marca que o usuário confirmou
            print("Confirmado!")                    # log para depuração
            layout_botao.content.value = "Cancelar" # volta o texto do botão para "Cancelar"
            # redefine o clique para iniciar a contagem novamente quando clicado no futuro
            layout_botao.on_click = lambda e: page.run_task(confirmar_acao, e)
            page.update()                           # atualiza a UI para refletir as mudanças
            action(e)                               # executa a ação externa passada (por exemplo: cancelar algo)

        # Função assíncrona que faz a contagem regressiva sem travar a interface
        async def confirmar_acao(e):
            nonlocal confirmado                     # permite alterar 'confirmado' dentro desta função
            confirmado = False                      # recomeça com confirmado = False (antes do usuário confirmar)
            layout_botao.on_click = acao_confirmada # durante a contagem, o próximo clique chama acao_confirmada
            # loop de contagem regressiva (10, 9, ..., 1)
            for i in range(10, 0, -1):
                if confirmado:                      # se o usuário clicou para confirmar, interrompe a contagem
                    break
                layout_botao.content.value = f"Confirma? ({i})"  # atualiza o texto para mostrar a contagem
                page.update()                       # atualiza a UI para mostrar o novo texto
                await asyncio.sleep(1)              # pausa 1 segundo de forma não bloqueante
            # quando a contagem termina (ou foi interrompida), volta ao estado inicial
            layout_botao.content.value = "Cancelar"
            layout_botao.on_click = lambda e: page.run_task(confirmar_acao, e)
            page.update()                           # atualiza a UI

        # Criação visual do botão com estilo simples
        layout_botao = ft.ElevatedButton(
            bgcolor="#9B3E3E",                                 # cor de fundo do botão
            content=ft.Text("Cancelar", size=16),              # texto inicial do botão
            color=ft.Colors.WHITE,                             # cor do texto
            on_click=lambda e: page.run_task(confirmar_acao, e),# ao clicar, inicia a contagem sem travar a UI
            height=50,                                         # altura do botão
            width=125,                                         # largura do botão
        )

        return layout_botao  # retorna o botão criado

    # Exemplo de função externa que será passada como 'action'
    def acao_cancelar(e):
        print("Ação externa executada! (por exemplo: voltar para outra tela)")

    # Cria o botão passando a função externa que deve rodar quando confirmado
    botao_cancelar = criar_botao_cancelar(acao_cancelar, page)

    page.add(botao_cancelar)  # adiciona o botão à página

ft.app(target=main)  # inicia o app Flet com a função main como entrypoint
