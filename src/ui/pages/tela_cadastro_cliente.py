import flet as ft
import re
from ui.components.botoes.botao_adicionar import criar_botao_adicionar
from ui.components.botoes.botao_cancelar import criar_botao_cancelar
from ui.components.botoes.botao_limpar_campos import criar_botao_limpar
from validate_docbr import CPF,CNPJ

def cadastrar_clientes(page, clientes, voltar_para_escolha):
    # Função que exibirá cada campo (CPF/CNPJ) com sua formatação própria.
    def selecionar_cpf_cnpj(e):
        if cpf_cnpj.value == "cpf": # Teste se o valor selecionado é "cpf"
            campo_cnpj.visible = False
            campo_cpf.visible = True

        elif cpf_cnpj.value == "cnpj": # Teste se o valor selecionado é "cpnj"
            campo_cpf.visible = False
            campo_cnpj.visible = True

        page.update()

    # Função que formatará o value to text field "telefone" para validar o nome permitindo apenas letras e espaços.:
    def formatar_nome(e):
        texto = e.control.value

        # Expressão regular que aceita letras (inclusive acentuadas) e espaços
        if re.fullmatch(r"[A-Za-zÀ-ÿ ]*", texto): # Aqui defino o padrão para A a Z maiúsculos, a a z minúsculos, letras com acentos e espaços, caso o usuário digite um número, dispara o alerta na tela.
            campo_nome.error_text = None
        else:
            campo_nome.error_text = "O nome deve conter apenas letras!" # Alerta que será mostrado na tela.

        # Remove espaços duplicados acidentalmente
        campo_nome.value = re.sub(r"\s{2,}", " ", texto) # Aqui ele substitui qualquer espaço que apareça 2 ou mais vezes ({2,}) por um espaço apenas (" ").

        page.update() # Atulaiza a página para mostrar as alterações.

    # Função que formatará o value to text field "telefone" para o formato de número de telefone:
    def formatar_telefone(e):
        # Filtra o que não é número (isdigit) na string (str), e junta ao texto apenas o que passar do filtro (filter).
        texto = "".join(filter(str.isdigit, e.control.value))

        # Limita o texto a 11 caracteres
        texto = texto[:11] # 0 a 10

        # Adiciona a máscara:
        formatado = "" # A string formatada começa vazia

        if len(texto) > 0: # Se o len de texto for maior que 0, junta o que foi digitado, dentro de parênteses.
            formatado = f"({texto[:2]}) "
        if len(texto) > 2: # Se for maior que 2, apenas junta o que foi digitado.
            formatado += texto[2:7]
        if len(texto) > 7: # Se for maior que 7, adiciona um traço antes e junta com o que foi digitado.
            formatado += "-" + texto[7:11]

        campo_telefone.value = formatado # Atualiza o que foi formatado já dentro do text field enquanto o usuário digita.   
        page.update() # Atualiza a página para que as alterações sejam mostradas.

    # Função que irá formatar o value do text field "cmapo_cpf" para o formato de cpf:
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

    # Função que irá formatar o value do text field "campo_cnpj" para o formato de cnpj:
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
    campo_nome = ft.TextField(label="Nome do cliente", bgcolor=ft.Colors.WHITE, width=610, autofocus=True, on_change=formatar_nome)

    campo_telefone = ft.TextField(label="Número de telefone do cliente", hint_text="Ex: (XX) XXXX-XXXX", bgcolor=ft.Colors.WHITE, width=610, on_change=formatar_telefone)

    # O campo de cadastro do cpf ou cnpj do cliente será diferente para cada tipo, mudando a formatação do campo de acordo com o dado que será diigtado.
    cpf_cnpj = ft.RadioGroup( # Grupo de seleção
        content=ft.Column( # O conteúdo é composto por uma coluna com as opções
            controls=[ # Os controles serão as opções
                ft.Radio(label="CPF", value="cpf"), # Opção cpf, altera o value da variável "cpf_cnpj" para cpf.

                ft.Radio(label="CNPJ", value="cnpj"), # Opção cnpj, altera o value da variável "cpf_cnpj" para "cnpj"
            ],
        ),

        value="cpf",
        on_change=selecionar_cpf_cnpj, # a cada mudança, chama a função de seleção.
    )

    # Campo para que o cpf seja digitado:
    campo_cpf = ft.TextField(label="CPF:", hint_text="EX: XXX.XXX.XXX-XX", visible=True, bgcolor=ft.Colors.WHITE, width=532, on_change=formatar_cpf, col={"xs": 12, "sm": 10, "md": 8, "lg": 2}) # A função de formatação funcionará em tempo de execução enquanto o usuário estiver digitando, sempre que houver uma maudança no Text Field, no caso, algum caracter a mais ou a menos, a função é acionada.

    # Campo para que o cnpj seja digitado:
    campo_cnpj = ft.TextField(label="CNPJ:", hint_text="EX: XX.XXX.XXX/YYYY-ZZ", visible=False, bgcolor=ft.Colors.WHITE, width=532, on_change=formatar_cnpj, col={"xs": 12, "sm": 10, "md": 8, "lg": 2})

    campos = [campo_nome, campo_telefone, campo_cpf, campo_cnpj]
    cpf_valid = CPF()
    cnpj_valid = CNPJ()

    def apenas_digitos(texto):
        return re.sub(r"\D", "", texto or "")

    def fechar_erro(e):
        page.close(erro)
        page.update()

    erro = ft.AlertDialog(
        title=ft.Text("Erro!", weight="bold"),

        content=ft.Container(
            content=ft.Text("Todos os campos devem estar preenchidos!", size=16, color="#9B3E3E"),
            width=300,
            height=50,
        ),

        actions=[
            ft.FilledButton(
                content=ft.Text("Ok", size=16),
                style=ft.ButtonStyle(bgcolor="#507656", color=ft.Colors.WHITE),
                on_click=fechar_erro,
            ),
        ],

        actions_alignment=ft.MainAxisAlignment.CENTER,
        bgcolor=ft.Colors.WHITE,
    )
        
    def adicionar_cliente(e):
        
        if not campo_nome.value or not campo_telefone.value or not campo_cpf.value and not campo_cnpj.value:
            page.open(erro)                
            page.update()
        
        else:
            if cpf_cnpj.value == "cpf": # se for escolhido cpf, adiciona o value do text field "campo_cpf"

                invalid = False
                if cpf_valid.validate(apenas_digitos(campo_cpf.value)):
                    novo_cliente = {
                        "nome":campo_nome.value,
                        "telefone":campo_telefone.value,
                        "cpf_cnpj":campo_cpf.value,
                        "editando":False,     
                    }

                else :
                    invalid = True
                    campo_cpf.error_text="CPF INVÁLIDO"
                    campo_cpf.focus()

            if cpf_cnpj.value == "cnpj": # Se for escolhido cnpj, adiciona o value do text field "campo_"
                invalid = False
                if cnpj_valid.validate(apenas_digitos(campo_cnpj.value)):
                    novo_cliente = {
                        "nome":campo_nome.value,
                        "telefone":campo_telefone.value,
                        "cpf_cnpj":campo_cnpj.value,
                    }

                else :
                    invalid = True
                    campo_cnpj.error_text="CNPJ INVÁLIDO"
                    campo_cnpj.focus()

            if invalid == False :
                clientes.append(novo_cliente)
                for campo in [campo_nome, campo_telefone, campo_cpf, campo_cnpj]:
                    campo.value = ""

                campo_cpf.error_text = None
                campo_cnpj.error_text = None
                campo_nome.focus()

        page.update()


    # Botões:
    botao_adicionar = criar_botao_adicionar(adicionar_cliente)
    botao_cancelar = criar_botao_cancelar(voltar_para_escolha, page)
    botao_limpar_campos = criar_botao_limpar(campos, page)


    # Layout:
    layout = ft.Container(
        content=ft.ResponsiveRow(
            controls=[
                # Será preciso adiconar cada campo dentro de um container porque o Textfield, não é redimensionável.
                # Nome
                ft.Column(
                    controls=[
                        # Nome
                        ft.Container(
                            content=campo_nome,
                            col={"xs": 12, "sm": 10, "md": 8, "lg": 6},
                            alignment=ft.alignment.center,
                        ),

                        # Número
                        ft.Container(
                            content=campo_telefone,
                            col={"xs": 12, "sm": 10, "md": 8, "lg": 6},
                            alignment=ft.alignment.center,
                        ),

                        ft.Container(
                            content=ft.Row(
                                    controls=[
                                        cpf_cnpj,
                                        campo_cpf,
                                        campo_cnpj,
                                    ],

                                    alignment=ft.MainAxisAlignment.CENTER
                                ),

                            col={"xs": 12, "sm": 10, "md": 8, "lg": 3},
                        ),
                    ],
                ),

                botao_cancelar,
                botao_limpar_campos,
                botao_adicionar,
            ],

            alignment=ft.MainAxisAlignment.CENTER,
            run_spacing=15,
            spacing=15,
        ),

        alignment=ft.alignment.center,
        expand=True,
        bgcolor="#E8E3DE",
        margin=0,
        padding=20,
        border_radius=15,
    )

    return layout
