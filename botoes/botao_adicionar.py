from flet import *

# Botão adicionar produtos: 
def botao_adcionar(action):
    return ElevatedButton(
        text= "Adicionar",
        bgcolor= Colors.BLUE_900,
        color= Colors.WHITE,
        on_click=action,
        height=50,
        width=110,
    ) 