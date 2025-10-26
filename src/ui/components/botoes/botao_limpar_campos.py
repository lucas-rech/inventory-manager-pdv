import flet as ft
import asyncio

def criar_botao_limpar(campos, page):
    confirmado = False

    # função que limpará os campos sempre que o usuário clicar no botão "limpar_campos"
    def limpar_campos(e):
        for c in campos: # para cada campo passado na lista de campos
            c.value = "" # Substitua o que estiver escrito por uma string vazia
            campos[0].focus() # Foque automaticamente no primeiro campo
            page.update() # Atualiza a tela 

    # Função executada quando o usuário confirma (clica novamente durante a contagem)
    def acao_confirmada(e):
        nonlocal confirmado # permite alterar a variável 'confirmado' que está no escopo externo.
        confirmado = True # marca que o usuário confirmou.

        layout_botao.content.value = "Cancelar" # volta o texto do botão para "Cancelar"
        layout_botao.on_click = lambda e: page.run_task(confirmar_acao, e) # redefine o clique para iniciar a contagem novamente quando clicado no futuro. (Se você passar direto confirmar_acao, vai dar erro do tipo AssertionError)

        page.update() # atualiza a UI para refletir as mudanças
        limpar_campos(e) # executa a ação externa passada (voltar_para_escolha)

    # Define uma função assíncrona. Para podermos usar await (parecido com o sleep) dentro dela.
    async def confirmar_acao(e):
        nonlocal confirmado # Aqui estou chamando o confirmado declarado acima, por issoo nonlocal.
        confirmado = False # Inicia como False
        layout_botao.on_click = acao_confirmada # Muda o evento do próximo click para a funcao de ação confirmada.

        # Loop de contagem regressiva:
        for i in range(10, 0, -1):
            if confirmado: # Se o usuário clicou para confirmar, interrompe a contagem.
                break

            layout_botao.content.value = f"Confirma? ({i})" # Atualiza o texto para mostrar a contagem.
            page.update() # Atualiza a tela para mostrar o novo texto.
            await asyncio.sleep(1) # Pausa 1 segundo sem travar a interface. (se fosse com o sleep, até que o loop não terminasse, a tela permaneceria "congelada".)

        # quando a contagem termina (ou foi interrompida), volta ao estado inicial
        layout_botao.content.value = "Cancelar" # O texto do botão volta para "Cancelar"
        layout_botao.on_click = lambda e: page.run_task(confirmar_acao, e) # A função que ele executará a ser clicado volta a ser confirmar_acao. (Se você passar direto confirmar_acao, vai dar erro do tipo AssertionError)
        page.update() # Atualiza a tela.

    layout_botao = ft.ElevatedButton(
        content= ft.Text("Limpar Campos", size=16),
        bgcolor= "#CFB757",
        color= ft.Colors.WHITE,
        on_click=lambda e: page.run_task(confirmar_acao, e), # ao clicar, inicia a contagem sem travar a UI. (Se você passar direto confirmar_acao, vai dar erro do tipo AssertionError)
        height=50,
        width=150,
    )

    return layout_botao