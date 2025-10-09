from flet import *

# Cabeçalho:
def criar_header(titulo=""): # Função que cria o cabeçalho da página, recebe o texto que será exibido como parâmetro.
    return Container(
        bgcolor= Colors.BLUE_900,
        padding= 20,
        content= Text(titulo, size= 35, weight= "bold", color= Colors.WHITE), 
        alignment= alignment.top_center,
        margin= 0,
    )
