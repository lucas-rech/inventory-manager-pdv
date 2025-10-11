import flet as ft

# Cabeçalho:
def criar_header(titulo=""): # Função que cria o cabeçalho da página, recebe o texto que será exibido como parâmetro.
    return ft.Container(
        bgcolor= ft.Colors.BLUE_900,
        padding= 20,
        content= ft.Text(titulo, size= 35, weight= "bold", color= ft.Colors.WHITE), 
        alignment= ft.alignment.top_center,
        margin= 0,
        border_radius=13
    )
