import flet as ft
import asyncio

def criar_popup(mensagem, page):
    popups = [] # Lista que irá conter todos os popups para caso mais de um precise aparecer na tela.

    async def mostrar_popup():
        pb = ft.ProgressBar(width=200, value=0) # Barra de progresso do popup.
        bottom_offset
        popup = ft.Container()