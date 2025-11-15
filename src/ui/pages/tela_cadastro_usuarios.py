import flet as ft

from ui.components.botoes.botao_adicionar import criar_botao_adicionar
from ui.components.botoes.botao_cancelar import criar_botao_cancelar

verificacao = False  # Variável global acessível por todas as funções

usuarios = {"admin": "admin", "": "",}

def primeiro_acesso(usuario, senha):
    global verificacao  # Declara que estamos usando a variável globalu

    if usuario.lower() in usuarios and senha.lower() == usuarios[usuario]:
        verificacao = True
    else:
        verificacao = False

    
def cadastro_usuarios(page, voltar_para_escolha):
    page.bgcolor = "#E8E3DE"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    # Campos de cadastro de usuário:
    nome = ft.TextField(label="Nome:", width=600, bgcolor=ft.Colors.WHITE)
    usuario = ft.TextField(label="Usuário:", width=600, bgcolor=ft.Colors.WHITE)
    tipo_de_usuario = ft.DropdownM2(
        label="Tipo de Usuário:",
        width=600,
        bgcolor=ft.Colors.WHITE,
        options=[
            ft.dropdownm2.Option("Administrador"),
            ft.dropdownm2.Option("Funcionário"),
        ]
    )
    senha = ft.TextField(label="Senha:", width=600, bgcolor=ft.Colors.WHITE, password=True, can_reveal_password=True)
    confirmar_senha = ft.TextField(label="Confirmar Senha:", width=600, bgcolor=ft.Colors.WHITE, password=True, can_reveal_password=True)

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


    def cadastrar(e):
        usuarios[usuario.value] = senha.value

        for campo in [nome, usuario, tipo_de_usuario, senha, confirmar_senha]:
            campo.value = ""

        page.update()

    botao_cancelar = criar_botao_cancelar(voltar_para_escolha, page)
    botao_cadastrar = criar_botao_adicionar(cadastrar) 

    alerta = ft.CupertinoAlertDialog(
        title=ft.Text("Aviso"),
        content=ft.Text(""),
        actions=[
            ft.CupertinoButton("OK", on_click=lambda e: fechar_alerta(e, page, alerta))
        ],
        modal=True,
    )

    def fechar_alerta(e, page, alerta):
        alerta.open = False
        page.update()

    if verificacao:
        return ft.Container(
            expand=True,
            bgcolor=ft.Colors.WHITE,
            margin=0,
            border_radius=15,
            content=ft.Container(
            padding=20,
            bgcolor="#507656",
            width=700,
            height=550,
            alignment=ft.alignment.center,
            border_radius=20,
            content=ft.Column(
                [
                    ft.Image(src="src/assets/Logo.jpg", width=150, height=150, fit=ft.ImageFit.CONTAIN, border_radius=10),
                    ft.Text("Cadastro de Usuário", size=30, weight="bold"),
                    nome,
                    usuario,
                    senha,
                    confirmar_senha,
                    botao_cadastrar,
                    alerta
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10,
            ),
        )
    )
    
    else:
        # Tela de cadastro de usuário:
        return ft.Container(
            expand=True,
            alignment=ft.alignment.center,
            margin=0,
            border_radius=15,
            content=ft.Column(
                    [
                        ft.Image(src="src/assets/Logo.jpg", width=150, height=150, fit=ft.ImageFit.CONTAIN, border_radius=10),
                        ft.Text("Cadastro de Usuário", size=30, weight="bold"),
                        nome,
                        usuario,
                        tipo_de_usuario,
                        senha,
                        confirmar_senha,
                        alerta,
                        ft.ResponsiveRow(
                            controls=[
                                botao_cancelar,
                                botao_cadastrar,
                            ],
                            alignment=ft.MainAxisAlignment.CENTER, 
                        ),
                    ],
                    
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=10,
                ),
            )
        
            
        