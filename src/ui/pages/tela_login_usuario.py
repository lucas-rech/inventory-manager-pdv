from flet import * # Lembrar de mudar o import para import flet as ft!

usuarios = ["admin"]
senhas = ["admin"]

def tela_login(page, entrar):

    page.bgcolor = "#E8E3DE"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    # Campos de login:
    usuario = TextField(label="Usuário:", width=300, bgcolor=Colors.WHITE)
    senha = TextField(label="Senha:", width=300, bgcolor=Colors.WHITE, password=True, can_reveal_password=True)

    # Lista de usuários válidos

    # Função que verifica se os campos foram preenchidos corretamente:
    def verificar_login(e):
        if usuario.value in usuarios and senha.value in senhas: # Verifica se o usuário e senha estão corretos
            entrar() # Chama a função entrar (que está em main.py) para entrar no sistema
        else:
            alerta.content.value = "Usuário ou senha incorretos!" # Se estiverem errados, mostra uma mensagem de erro
            alerta.open = True # Abre o alerta
            page.update() # Atualiza a página para mostrar o alerta

    botao_entrar = ElevatedButton("Entrar", on_click=verificar_login, width=300, height=40, bgcolor="#E8E3DE", color="#507656")

    alerta = CupertinoAlertDialog(
        title=Text("Erro"),
        content=Text(""),
        actions=[
            CupertinoButton("OK", on_click=lambda e: fechar_alerta(e, page, alerta))
        ],
        modal=True,
    )

    def fechar_alerta(e, page, alerta):
        alerta.open = False
        page.update()

    # Tela de login:
    return Container(
        padding=20,
        width=650,
        height=450,
        bgcolor="#507656",
        alignment=alignment.center,
        border_radius=20,
        content=Column(
            [
                Image(src="src/assets/Logo.jpeg", width=150, height=150, fit=ImageFit.CONTAIN),
                Text("Login", size=40, weight="bold"),
                usuario,
                senha,
                botao_entrar,
                alerta
            ],
            alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            spacing=10,
        ),
    )