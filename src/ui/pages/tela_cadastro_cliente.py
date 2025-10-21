import flet as ft
from ui.components.botoes.botao_adicionar import criar_botao_adicionar
from ui.components.botoes.botao_cancelar import criar_botao_cancelar

def cadastrar_clientes(page, clientes):
    # Função que exibirá cada campo (CPF/CNPJ) com sua formatação própria.
    def selecionar_cpf_cnpj(e):
        if cpf_cnpj.value == "cpf": # Teste se o valor selecionado é "cpf"
            campo_cnpj.visible = False
            campo_cpf.visible = True

        elif cpf_cnpj.value == "cnpj": # Teste se o valor selecionado é "cpnj"
            campo_cpf.visible = False
            campo_cnpj.visible = True

        page.update()


    # Campos do formulário para o cadastro de um cliente:
    nome = ft.TextField(label="Nome do cliente", bgcolor=ft.Colors.WHITE, width=610)

    numero = ft.TextField(label="Número de telefone do cliente", hint_text="Ex: (XX) XXXX-XXXX", bgcolor=ft.Colors.WHITE, width=610)

    # O campo de cadastro do cpf ou cnpj do cliente será diferente para cada tipo, mudando a formatação do campo de acordo com o dado que será diigtado.
    cpf_cnpj = ft.RadioGroup( # Grupo de seleção
        content=ft.Column( # O conteúdo é composto por uma coluna com as opções
            controls=[ # Os controles serão as opções
                ft.Radio(label="CPF", value="cpf"), # Opção cpf, altera o value da variável "cpf_cnpj" para cpf.

                ft.Radio(label="CNPJ", value="cnpj"), # Opção cnpj, altera o value da variável "cpf_cnpj" para "cnpj"
            ]
        ),

        value="cpf",
        on_change=selecionar_cpf_cnpj, # a cada mudança, chama a função de seleção.
    )

    # Campo para que o cpf seja digitado:
    campo_cpf = ft.TextField(label="CPF:", hint_text="EX: XXX.XXX.XXX-XX", visible=True, bgcolor=ft.Colors.WHITE, width=532)

    # Campo para que o cnpj seja digitado:
    campo_cnpj = ft.TextField(label="CNPJ:", hint_text="EX: XX.XXX.XXX/YYYY-ZZ", visible=False, bgcolor=ft.Colors.WHITE, width=532)

    def adicionar_cliente(e):
        novo_cliente = {
            "nome":nome.value,
            "numero":numero.value,
        }

        clientes.append(novo_cliente)
        print(clientes)

        for campo in [nome, numero]:
            campo.value = ""

        page.update()

    botao_adicionar = criar_botao_adicionar(adicionar_cliente)
    botao_cancelar = criar_botao_cancelar(True)

    layout = ft.Container(
        ft.Column(
            [
                ft.Row([nome], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([numero], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([cpf_cnpj, campo_cpf, campo_cnpj], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([botao_adicionar, botao_cancelar], alignment=ft.MainAxisAlignment.CENTER),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ), 

        expand=True,
        bgcolor="#E8E3DE",
        margin=0,
        border_radius=15,
    )

    return layout
