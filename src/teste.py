import flet as ft
import asyncio

async def main(page: ft.Page):
    popups = []  # aqui guardamos as barras ativas

    async def criar_popup():
        # índice da nova barra
        idx = len(popups)

        pb = ft.ProgressBar(width=200, value=0)

        # calculo do bottom para empilhar dinamicamente
        bottom_offset = 20 + (idx * 80)

        container_pb = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("Venda Realizada!", size=18, color=ft.Colors.WHITE),
                    pb,
                ],
                alignment=ft.CrossAxisAlignment.CENTER,
            ),
            width=300,
            bgcolor="#85a289",
            opacity=0.6,
            right=20,
            bottom=bottom_offset,
        )

        # adiciona à lista antes de exibir
        popups.append(container_pb)

        page.add(container_pb)
        page.update()

        # animação da barra
        for i in range(101):
            pb.value = i / 100
            page.update()
            await asyncio.sleep(0.02)

        # remover após terminar
        page.controls.remove(container_pb)
        popups.remove(container_pb)

        # reimprimir offsets dos restantes
        for idx, c in enumerate(popups):
            c.bottom = 20 + (idx * 80)

        page.update()

    async def iniciar(e):
        # dispara uma nova barra de progresso (não bloqueia as outras)
        asyncio.create_task(criar_popup())

    btn = ft.ElevatedButton("Iniciar", on_click=iniciar)

    page.add(btn)

ft.app(target=main)
