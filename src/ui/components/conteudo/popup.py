import flet as ft
import asyncio

popups = [] # Lista que irá conter todos os popups para caso mais de um precise aparecer na tela.

async def criar_popup(mensagem, page):
    pb = ft.ProgressBar(width=200, value=0, color="#507656") # Barra de progresso do popup. Começa no valor 0 == 0%.
    bottom_offset = 20 + (len(popups) * 95) # Aqui vai ser a variável que irá definir a distância do popup da borda de baixo da janela, já que eles serão empilhados com uma distância de 80 pixeis um do outro.

    popup = ft.Container(
        content=ft.Column(
            controls=[
                ft.Row([ft.Text(f"{mensagem}", size=18, color=ft.Colors.WHITE)], alignment=ft.MainAxisAlignment.CENTER), # Texto que seá exibido no popup
                pb,
            ],

            alignment=ft.CrossAxisAlignment.CENTER
        ),

        width=250,
        bgcolor="#765070",
        opacity=0.50,
        right=30,
        bottom=bottom_offset, # Aqui passamos a distância já calculada.
        padding=25,
        border_radius=10,
    )

    popups.append(popup) # Adiciona o popup à lista de popups ativos.
    page.overlay.append(popup) # Adiciona o popup à uma camada acima da página atual.
    page.update() # atualiza a página.


    for i in range(101): 
        pb.value = i/100 # calcula a porcentagem de progresso da barra.
        page.update() # Atualiza a página.
        await asyncio.sleep(0.02) # Espera 2 milissegundos para dar mais uma volta no loop, no fim dá mais ou menos 2 segundos de permanência do popup na tela.

    page.overlay.remove(popup) # Remove da camada acima da página.
    popups.remove(popup) # remove da lista de popups ativos.

    for i, p in enumerate(popups):
        p.bottom = 30 + (i * 95)

    page.update()
