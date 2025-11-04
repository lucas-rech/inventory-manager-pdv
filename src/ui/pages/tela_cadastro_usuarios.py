from flet import *

verificacao = False  # Variável global acessível por todas as funções

def primeiro_acesso(usuario, senha):
    global verificacao  # Declara que estamos usando a variável global
    usuarios = ["admin"]
    senhas = ["admin"]

    if usuario.lower() in usuarios and senha.lower() in senhas:
        verificacao = True
    else:
        verificacao = False

    
def cadastro_usuarios(page: Page):
    page.bgcolor = "#E8E3DE"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    # Campos de cadastro de usuário:
    nome = TextField(label="Nome:", width=300, bgcolor=Colors.WHITE)
    usuario = TextField(label="Usuário:", width=300, bgcolor=Colors.WHITE)
    tipo_de_usuario = DropdownM2(
        label="Tipo de Usuário:",
        width=300,
        bgcolor=Colors.WHITE,
        options=[
            dropdownm2.Option("Administrador"),
            dropdownm2.Option("Funcionário"),
        ]
    )
    senha = TextField(label="Senha:", width=300, bgcolor=Colors.WHITE, password=True, can_reveal_password=True)
    confirmar_senha = TextField(label="Confirmar Senha:", width=300, bgcolor=Colors.WHITE, password=True, can_reveal_password=True)

    # Função que verifica se os campos foram preenchidos corretamente:
    def verificar_cadastro(e):
        if not nome.value or not usuario.value or not senha.value or not confirmar_senha.value:
            alerta.content.value = "Por favor, preencha todos os campos!" # Verifica se todos os campos foram preenchidos
            alerta.open = True
            page.update()
        elif senha.value != confirmar_senha.value:
            alerta.content.value = "As senhas não coincidem!" # Verifica se as senhas coincidem
            alerta.open = True
            page.update()
        else:
            alerta.content.value = "Usuário cadastrado com sucesso!" # Se tudo estiver correto, mostra uma mensagem de sucesso
            alerta.open = True
            page.update()
            # Aqui deveria ser colocado o código para cadastrar o usuário no banco de dados
            # tela_login.usuarios.append(usuario.value) # Adiciona o novo usuário à lista de usuários válidos
            # tela_login.senhas.append(senha.value)

    botao_cadastrar = ElevatedButton("Cadastrar", on_click=verificar_cadastro, width=300, bgcolor="#4CAF50", color=Colors.WHITE)

    alerta = CupertinoAlertDialog(
        title=Text("Aviso"),
        content=Text(""),
        actions=[
            CupertinoButton("OK", on_click=lambda e: fechar_alerta(e, page, alerta))
        ],
        modal=True,
    )

    def fechar_alerta(e, page, alerta):
        alerta.open = False
        page.update()

    if verificacao:
        return Container(
        padding=20,
        bgcolor="#507656",
        width=700,
        height=550,
        alignment=alignment.center,
        border_radius=20,
        content=Column(
            [
                Image(src="src/assets/Logo.jpeg", width=150, height=150, fit=ImageFit.CONTAIN, border_radius=10),
                Text("Cadastro de Usuário", size=30, weight="bold"),
                nome,
                usuario,
                senha,
                confirmar_senha,
                botao_cadastrar,
                alerta
            ],
            alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            spacing=10,
        ),
    )
    
    else:
        # Tela de cadastro de usuário:
        return Container(
            padding=20,
            bgcolor="#507656",
            width=700,
            height=600,
            alignment=alignment.center,
            border_radius=20,
            content=Column(
                [
                    Image(src="src/assets/Logo.jpeg", width=150, height=150, fit=ImageFit.CONTAIN, border_radius=10),
                    Text("Cadastro de Usuário", size=30, weight="bold"),
                    nome,
                    usuario,
                    tipo_de_usuario,
                    senha,
                    confirmar_senha,
                    botao_cadastrar,
                    alerta
                ],
                alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                spacing=10,
            ),
        )