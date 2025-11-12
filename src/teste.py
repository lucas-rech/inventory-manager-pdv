import flet as ft
import asyncio

async def main(page: ft.Page):
    popups = []  # guardamos os popups ativos

    async def criar_popup():
        idx = len(popups)

        pb = ft.ProgressBar(width=200, value=0)

        # cálculo do offset vertical
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
            padding=15,
            border_radius=10,
        )

        # adiciona o popup ao overlay
        popups.append(container_pb)
        page.overlay.append(container_pb)
        page.update()

        # animação da progress bar
        for i in range(101):
            pb.value = i / 100
            page.update()
            await asyncio.sleep(0.02)

        # remove o popup após término
        page.overlay.remove(container_pb)
        popups.remove(container_pb)

        # reordena os popups restantes
        for idx, c in enumerate(popups):
            c.bottom = 20 + (idx * 80)

        page.update()

    async def iniciar(e):
        asyncio.create_task(criar_popup())

    btn = ft.ElevatedButton("Iniciar", on_click=iniciar)

    page.add(btn)

ft.app(target=main)
