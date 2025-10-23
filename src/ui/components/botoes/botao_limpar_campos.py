import flet as ft

def criar_botao_limpar(campos, page): # Adcionar confirmação para a limpeza dos campos (Ex: Tem certeza? (Contagem de 10 segundos))
    def limpar_campos(e):
        for c in campos:
            c.value = ""
            campos[0].focus()
            page.update()

    return ft.ElevatedButton(
        content= ft.Text("Limpar Campos", size=16),
        bgcolor= "#CFB757",
        color= ft.Colors.WHITE,
        on_click=limpar_campos,
        height=50,
        width=150,
    )