import flet as ft

usuarios = ["admin"]
senhas = ["admin"]

def criar_tela_login(page, entrar):

    page.bgcolor = "#E8E3DE"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    # Campos de login:
    usuario = ft.TextField(label="Usuário:", width=300, bgcolor=ft.Colors.WHITE, autofocus=True)
    senha = ft.TextField(label="Senha:", width=300, bgcolor=ft.Colors.WHITE, password=True, can_reveal_password=True)

    # Lista de usuários válidos

    # Função que verifica se os campos foram preenchidos corretamente:
    def verificar_login(e):
        if usuario.value in usuarios and senha.value in senhas: # Verifica se o usuário e senha estão corretos
            entrar() # Chama a função entrar (que está em main.py) para entrar no sistema
        else:
            alerta.content.value = "Usuário ou senha incorretos!" # Se estiverem errados, mostra uma mensagem de erro
            alerta.open = True # Abre o alerta
            page.update() # Atualiza a página para mostrar o alerta

    botao_entrar = ft.ElevatedButton("Entrar", on_click=verificar_login, width=300, height=40, bgcolor="#E8E3DE", color="#507656")

    alerta = ft.CupertinoAlertDialog(
        title=ft.Text("Erro"),
        content=ft.Text(""),
        actions=[
            ft.CupertinoButton("OK", on_click=lambda e: fechar_alerta(e, page, alerta))
        ],
        modal=True,
    )

    def fechar_alerta(e, page, alerta):
        alerta.open = False
        page.update()

    # Tela de login:
    return ft.Container(
        padding=20,
        width=650,
        height=450,
        bgcolor="#507656",
        alignment=ft.alignment.center,
        border_radius=20,
        content=ft.Column(
            [
                ft.Image(src="src/assets/Logo.jpeg", width=150, height=150, fit=ft.ImageFit.CONTAIN),
                ft.Text("Login", size=40, weight="bold"),
                usuario,
                senha,
                botao_entrar,
                alerta
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10,
        ),
    )