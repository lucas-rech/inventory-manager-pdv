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

    # Função que irá formatar o value do text field para o formato de cpf:
    def formatar_cpf(e):
        # Filtra o que não é número (isdigit) na string (str), e junta ao texto apenas o que passar do filtro (filter).
        texto = "".join(filter(str.isdigit, e.control.value))

        # Limita o texto a 11 caracteres
        texto = texto[:11] # 0 até 10

        # Adiciona a máscara:
        formatado = "" # A string formatada começa vazia.

        # A lógica basicamente funciona pegando a string que foi digitada no text field e separando em setores de 3 dígitos para que seja adicionados os pontos e o traço final.
        if len(texto) > 0:
            formatado = texto[:3] # Se o len de texto for maior que 0, apenas junta o que foi digitado.
        if len(texto) > 3:
            formatado += "." + texto[3:6] # Se for maior que 3, adiciona um ponto antes e junta com o que foi digitado.
        if len(texto) > 6:
            formatado += "." + texto[6:9] # Se for maior que 6, adiciona um ponto antes e junta com o que foi digitado.
        if len(texto) > 9:
            formatado += "-" + texto[9:11]

        campo_cpf.value = formatado # Atualiza o que foi formatado já dentro do text field enquanto o usuário digita.   
        page.update() # Atualiza a página para que as alterações sejam mostradas.

    # Função que irá formatar o value do text field para o formato de cnpj:
    def formatar_cnpj(e):
        # Filtra o que não é número (isdigit) na string (str), e junta ao texto apenas o que passar do filtro (filter).
        texto = "".join(filter(str.isdigit, e.control.value))

        # Limita o texto a 14 caracteres
        texto = texto[:14] # 0 até 13

        # Adiciona a máscara:
        formatado = "" # A string formatada começa vazia.

        # A lógica basicamente funciona pegando a string que foi digitada no text field e separando em setores de 3 dígitos para que seja adicionados os pontos, o   "/0001" e o traço final.
        if len(texto) > 0:
            formatado = texto[:2]
        if len(texto) > 2:
            formatado += "." + texto[2:5]
        if len(texto) > 5:
            formatado += "." + texto[5:8]
        if len(texto) > 8:
            formatado += "/" + texto[8:12]
        if len(texto) > 12:
            formatado += "-" + texto[12:14]

        campo_cnpj.value = formatado # Atualiza o que foi formatado já dentro do text field enquanto o usuário digita.   
        page.update() # Atualiza a página para que as alterações sejam mostradas.


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
    campo_cpf = ft.TextField(label="CPF:", hint_text="EX: XXX.XXX.XXX-XX", visible=True, bgcolor=ft.Colors.WHITE, width=532, on_change=formatar_cpf) # A função de formatação funcionará em tempo de execução enquanto o usuário estiver digitando, sempre que houver uma maudança no Text Field, no caso, algum caracter a mais ou a menos, a função é acionada.

    # Campo para que o cnpj seja digitado:
    campo_cnpj = ft.TextField(label="CNPJ:", hint_text="EX: XX.XXX.XXX/YYYY-ZZ", visible=False, bgcolor=ft.Colors.WHITE, width=532, on_change=formatar_cnpj)

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
