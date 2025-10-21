import flet as ft

def main(page: ft.Page):
    txt = ft.TextField(label="Idade")

    def validar(e):
        if not txt.value.isdigit():
            txt.error_text = "Digite apenas números"
        else:
            txt.error_text = None
        page.update()

    btn = ft.ElevatedButton("Validar", on_click=validar)
    page.add(txt, btn)

ft.app(target=main)
