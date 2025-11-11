import flet as ft
import re
import datetime
from ui.components.botoes.botao_adicionar import criar_botao_adicionar
from ui.components.botoes.botao_cancelar import criar_botao_cancelar
from ui.components.botoes.botao_limpar_campos import criar_botao_limpar


# Função que criará a tela de cadastro de produto
def cadastrar_produtos(page, produtos, voltar_para_escolha):
    # Função que fará a verificação da opção do cálculo do preço de venda escolhida.
    def selecionar_porcentagem(e):
        if porcentagem_preco_venda.value == "porcentagem": # Teste se o valor selecionado é "porcentagem"
            porcentagem.visible = True
            preco_venda.read_only = True

        if porcentagem_preco_venda.value == "manual": # Teste se o valor selecionado é "manual"
            porcentagem.visible = False
            preco_venda.read_only = False

        page.update()

    # Função que formatará o código inserido no campo código.
    def formatar_codigo(e):
        texto = "".join(filter(str.isdigit, e.control.value)) # Filtra para que apenas números sejam adicionados à string.
        texto = texto[:13]
        codigo.value = texto # Atualiza enquanto o usuário digita com o valor formatado.
        page.update() # Atualiza a página para mostrar as alterações.

    # Função que formatará o nome inserido no campo nome.
    def formatar_nome(e): 
        texto = e.control.value
        texto = texto[:90]
         
        # Remove espaços duplicados acidentalmente
        nome.value = re.sub(r"\s{2,}", " ", texto) # Aqui ele substitui qualquer espaço que apareça 2 ou mais vezes ({2,}) por um espaço apenas (" ").
        page.update() # Atulaiza a página para mostrar as alterações.

    # Função que formatará o preco de custo inserido no campo preco_custo.
    def formatar_preco_custo(e):
        texto = "".join(filter(str.isdigit, e.control.value))
        texto = texto[:11]

        if not texto:
            preco_custo.value = "R$ 0,00"
            page.update()
            return # O return está vazio aqui para quefuncione como um "Break" da função, ou seja para aqui.

        # Converte para inteiro e divide por 100 para colocar vírgula decimal
        valor = int(texto) / 100

        # Formata com separador de milhar (.) e decimal (,)
        formatado = f"R$ {valor:,.2f}".replace(",", "v").replace(".", ",").replace("v", ".") # A ideia aqui é usar uma letra provisória (v) pra segurar o lugar das vírgulas, e só depois trocar tudo certinho.
        # essa troca dupla inverte o padrão americano (1,234.56 → 1.234,56)

        preco_custo.value = formatado # Atualiza enquanto o usuário digita com o valor formatado.
        page.update() # Atualiza a página para mostrar as alterações.

    def formatar_preco_venda(e):
        # Remove o "R$" e os pontos do preço de custo, troca vírgula por ponto para converter em float
        custo_texto = preco_custo.value.replace("R$ ", "").replace(".", "").replace(",", ".")

        try:
            custo = float(custo_texto) # Converte o texto para número decimal (float)
        except ValueError:
            custo = 0.0 # Se der algum erro (por exemplo, o campo estiver vazio ou com texto inválido), usamos custo = 0.0

        if porcentagem_preco_venda.value == "porcentagem": # Se a opção de cálculo for inserindo a porcentagem.
            p_texto = "".join(filter(str.isdigit, porcentagem.value)) # Adiciona ao texto da variavel "p_texto" apenas o que for numero.

            if p_texto: # Se p_texto == True, ou seja, tem algo
                lucro = int(p_texto) / 100 # Trasforma em int e divide a porcentagem digitada por 100
                valor = custo * (1 + lucro) # Multiplica pelo preco de custo a porcentagem digitada.

            else: # Senão, apenas passa o preço de custo como preço de venda
                valor = custo

        else:  # Se a opção de cálculo for inserindo manualmente
            p_texto = "".join(filter(str.isdigit, preco_venda.value)) # Adiciona ao texto da variavel "p_texto" apenas o que for numero.

            if p_texto: # Se p_texto == True, ou seja, tem algo
                valor = int(p_texto) / 100 # Converte para int e divide por 100 para conseguir os dois dígitos dos centavos.
            
            else: # Senão, apenas passa o preço de custo como preço de venda
                valor = custo

        # Formata com separador de milhar e decimal
        formatado = f"R$ {valor:,.2f}".replace(",", "v").replace(".", ",").replace("v", ".")
        preco_venda.value = formatado
        page.update()

    def formatar_quantidade(e):
        texto = "".join(filter(str.isdigit, e.control.value))
        texto = texto[:5]
        quantidade.value = texto
        page.update()

    def formatar_validade(e):
        texto = "".join(filter(str.isdigit, e.control.value))
        texto = texto[:8]
        
        formatado = ""

        if len(texto) > 0:
            formatado += texto[:2]
        if len(texto) > 2:
            formatado += "/" + texto[2:4]
        if len(texto) > 4:
            formatado += "/" + texto[4:8]

        validade.value = formatado
        page.update()

    def handle_change(e):
        # Atualiza o TextField com a data selecionada formatada
        data_formatada = e.control.value.strftime('%d/%m/%Y')
        validade.value = data_formatada
        validade.update()
        page.close(date_picker)

    def handle_dismissal(e):
        # Ação quando o DatePicker é fechado sem selecionar
        page.close(date_picker)

    # Cria o DatePicker com as configurações
    date_picker = ft.DatePicker(
        first_date=datetime.datetime(year=2025, month=1, day=1),
        last_date=datetime.datetime.today() + datetime.timedelta(90),
        on_change=handle_change,
        on_dismiss=handle_dismissal,
    )

    def abrir_datepicker(e):
        # Abre o DatePicker quando clicar no botão ou no campo
        page.open(date_picker)


    # Campos do formulário:
    codigo = ft.TextField(label= "Código:", width=610, bgcolor=ft.Colors.WHITE, on_change=formatar_codigo)
    nome = ft.TextField(label= "Nome do Produto:", width=610, bgcolor=ft.Colors.WHITE, on_change=formatar_nome) 
    preco_custo = ft.TextField(label= "Preço de Custo:", bgcolor=ft.Colors.WHITE, width=610, on_change=formatar_preco_custo)
    preco_venda = ft.TextField(label= "Preço de venda:", bgcolor=ft.Colors.WHITE, width=610, read_only=True, on_change=formatar_preco_venda)
    quantidade = ft.TextField(label= "Quantidade:", bgcolor=ft.Colors.WHITE, width=610, on_change=formatar_quantidade)
    validade = ft.TextField(label= "Validade:", bgcolor=ft.Colors.WHITE, width=560, on_change=formatar_validade)
    selecionar_data = ft.IconButton(icon=ft.Icons.CALENDAR_MONTH, on_click=abrir_datepicker, icon_color=ft.Colors.BLACK)
    
    porcentagem = ft.TextField(label= "Porcentagem de lucro:", bgcolor=ft.Colors.WHITE, width=610, visible=True, on_change=formatar_preco_venda)

    campos = [codigo, nome, preco_custo, preco_venda, quantidade, validade, porcentagem]

    porcentagem_preco_venda = ft.RadioGroup(
        content=ft.Column(
            controls=[
                ft.Radio(label="Porcentagem", value="porcentagem"),
                ft.Radio(label="Manual", value="manual"),
            ],
        ),

        value="porcentagem",
        on_change=selecionar_porcentagem,
    )

    # Função que adicionará os items ao estoque:
    def adicionar_produto(e):
        novo_produto = { # Adiciona os valores digitados em cada campo às respectivas chaves no dicionário.
            "codigo":codigo.value,
            "nome":nome.value,
            "preco_custo":preco_custo.value,
            "preco_venda":preco_venda.value,
            "quantidade":quantidade.value,
            "validade":validade.value,
            "editando":False,
        }

        produtos.append(novo_produto) # Adiciona todas as informações do produto à lista "produtos".

        for campo in [codigo, nome, preco_custo, preco_venda, quantidade, validade, porcentagem]:
            campo.value = "" # Limpa todos os campos, substituindo o que foi digitado por uma string vazia ("").

        page.update() # Atualiza a página para mostrar o que foi alterado.


    botao_adicionar = criar_botao_adicionar(adicionar_produto)
    botao_cancelar = criar_botao_cancelar(voltar_para_escolha, page)
    botao_limpar_campos = criar_botao_limpar(campos, page)

    # Tela onde serão inseridas as informações dos produtos:
    tela_informacoes_produto = ft.Container(
        ft.Column(
            [
                ft.Row([codigo, nome], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([quantidade, validade, selecionar_data], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([preco_custo, preco_venda], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([porcentagem_preco_venda, porcentagem], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([botao_adicionar, botao_limpar_campos, botao_cancelar], alignment=ft.MainAxisAlignment.CENTER),
            ],

            alignment=ft.MainAxisAlignment.CENTER,
            spacing=15,
        ),

        expand=True,
        bgcolor=ft.Colors.WHITE,
        margin=0,
        border_radius=15,
    )

    return tela_informacoes_produto
