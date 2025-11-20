import flet as ft
import re
import datetime
import asyncio

# Função que irá criar a tela de estoque:
def criar_tela_estoque(produtos, page):
    # Tabela dos itens em estoque:
    tabela_estoque = ft.DataTable(
        columns=[ # Define as 6 colunas que terão dados (Código, Nome, Preço de custo, Preço de venda, Quantidade e Validade)
            ft.DataColumn(ft.Text("Código de Barras", size=16)),
            ft.DataColumn(ft.Text("Nome", size=16)),
            ft.DataColumn(ft.Text("Preço de custo", size=16)),
            ft.DataColumn(ft.Text("Preço de venda", size=16)),
            ft.DataColumn(ft.Text("Quantidade", size=16)),
            ft.DataColumn(ft.Text("Validade", size=16)),
            ft.DataColumn(ft.Text("Ações", size=16))
        ],

        rows=[], # As linhas começam vazias, sem nenhum item em estoque.

        width=1500,
    )

    # Função que adicionará itens à tabela de estoque:
    def atualizar(): 
        tabela_estoque.rows.clear() # Limpa todas as tabelas anteriores para atualizar tudo do zero.

        for i, produto in enumerate(produtos): # Para cada indice da lista "produtos"
            botao_editar = ft.IconButton(
                icon=ft.Icons.EDIT,
                style=ft.ButtonStyle(color="#507656"), # Cor do botão.
                on_click=lambda e, index=i: editar(index), # Quando for clicado: passa o valor de i par ao parâmetro index da função editar e chama a função editar.
            )
            
            tabela_estoque.rows.append( # Cria uma nova linha na tabela

                ft.DataRow( # Cada linha/row (neste caso DataRow por ser a linha de uma tabela) é feita de várias células (DataCell), uma para cada coluna.
                    cells=[
                        ft.DataCell(ft.Text(produto["codigo"], size=14)), # Busca o valor atráves do nome no dicionário da função adicionar produto.
                        ft.DataCell(ft.Text(produto["nome"], size=14)),
                        ft.DataCell(ft.Text(produto["preco_custo"], size=14)),
                        ft.DataCell(ft.Text(produto["preco_venda"], size=14)),
                        ft.DataCell(ft.Text(produto["quantidade"], size=14)),
                        ft.DataCell(ft.Text(produto["validade"], size=14)),
                        ft.DataCell(botao_editar),
                    ]
                )
            ) 

        page.update() # Atualiza a página para mostrar as alterações.

    atualizar()







    # FUNÇÕES DE EDIÇÃO DA TABELA:
    # Função de editar dados da tabela:
    def editar(index): # Recebe o index dos dados que serão editados.
        campo_codigo_barras.value = produtos[index]["codigo"]
        campo_nome_produto.value = produtos[index]["nome"]
        campo_preco_custo.value = produtos[index]["preco_custo"]
        campo_preco_venda.value = produtos[index]["preco_venda"]
        campo_quantidade.value = produtos[index]["quantidade"]
        campo_validade.value = produtos[index]["validade"]

        page.open(janela_editar) # Abre a janela de edição dos dados.

        nonlocal index_editado
        index_editado = index

        atualizar() # Atualiza a tabela.

    # Função de salvar os novos dados na tabela:
    def salvar(index, campo_codigo_barras, campo_nome_produto, campo_preco_custo, campo_preco_venda, campo_quantidade, campo_validade): # Recebe os campos que recebem as novas informações.
        if not campo_codigo_barras.value or not campo_nome_produto.value or not campo_preco_custo.value or not campo_preco_venda.value or not campo_quantidade.value or not campo_validade.value:
            page.open(erro) # Mensagem de erro
            page.update()

        else:
            produtos[index]["codigo"] = campo_codigo_barras.value # Muda o dado contido na chave codigo, no index passado.
            produtos[index]["nome"] = campo_nome_produto.value # Muda o dado contido na chave nome, no index passado.
            produtos[index]["preco_custo"] = campo_preco_custo.value # Muda o dado contido na chave preco_custo, no index passado.
            produtos[index]["preco_venda"] = campo_preco_venda.value # Muda o dado contido na chave preco_venda, no index passado.
            produtos[index]["quantidade"] = campo_quantidade.value # Muda o dado contido na chave quantidade, no index passado.
            produtos[index]["validade"] = campo_validade.value # Muda o dado contido na chave validade, no index passado.

            page.close(janela_editar)
            page.update()

            atualizar() # Atualiza a tabela.

    
    def fechar_erro(e):
        page.close(erro)
        page.update()
        page.run_task(reabrir_edicao)

    async def reabrir_edicao():
        await asyncio.sleep(0.05)
        page.open(janela_editar)
        page.update()


    # Função que irá cancelar as alterações:
    def cancelar(e): # Recebe o index de onde a alteração está sendo feita.
        page.close(janela_editar)
        page.update()
        atualizar() # Atualiza a tabela.









    # FUNÇÕES DE FORMATAÇÃO DOS DADOS DA TABELA: 
    def formatar_codigo_barras(e):
        texto = "".join(filter(str.isdigit, e.control.value))
        campo_codigo_barras.value = texto
        page.update()

    def formatar_nome_produto(e):
        texto = e.control.value
        texto = texto[:80]
        
        campo_nome_produto.value = re.sub(r"\s{2,}", " ", texto)
        page.update()

    def formatar_preco_custo(e):
        texto = "".join(filter(str.isdigit, e.control.value))

        if not texto:
            campo_preco_custo.value = "R$ 0,00"
            page.update()
            return # O return está vazio aqui para quefuncione como um "Break" da função, ou seja para aqui.

        # Converte para inteiro e divide por 100 para colocar vírgula decimal
        valor = int(texto) / 100

        # Formata com separador de milhar (.) e decimal (,)
        formatado = f"R$ {valor:.2f}".replace(",", "v").replace(".", ",").replace("v", ".") # A ideia aqui é usar uma letra provisória (v) pra segurar o lugar das vírgulas, e só depois trocar tudo certinho.
        # essa troca dupla inverte o padrão americano (1,234.56 → 1.234,56)

        campo_preco_custo.value = formatado
        page.update()

    def formatar_quantidade(e):
        texto = "".join(filter(str.isdigit, e.control.value))
        texto = texto[:5]
        campo_quantidade.value = texto
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

        campo_validade.value = formatado
        page.update()








    # CAMPOS DE EDIÇÃO DA TABELA:
    campo_codigo_barras = ft.TextField(
        label="Código de Barras",
        value="",
        width=100,
        on_change=formatar_codigo_barras,
    )

    campo_nome_produto = ft.TextField(
        label="Nome:",
        width=120,
        value="",
        on_change=formatar_nome_produto,
    )

    campo_preco_custo = ft.TextField(
        label="Preço de Custo:",
        width=120,
        value="",
        on_change=formatar_preco_custo,
    )

    # Função que fará a verificação da opção do cálculo do preço de venda escolhida.
    def selecionar_porcentagem(e):
        if porcentagem_preco_venda.value == "porcentagem": # Teste se o valor selecionado é "porcentagem"
            porcentagem.visible = True
            campo_preco_venda.read_only = True

        if porcentagem_preco_venda.value == "manual": # Teste se o valor selecionado é "manual"
            porcentagem.visible = False
            campo_preco_venda.read_only = False

        page.update()

    def formatar_preco_venda(e):
        # Remove o "R$" e os pontos do preço de custo, troca vírgula por ponto para converter em float
        custo_texto = campo_preco_custo.value.replace("R$ ", "").replace(".", "").replace(",", ".")

        try:
            custo = float(custo_texto) # Converte o texto para número decimal (float)
        except ValueError:
            custo = 0.0 # Se der algum erro (por exemplo, o campo estiver vazio ou com texto inválido), usamos custo = 0.0

        p_texto = "".join(filter(str.isdigit, porcentagem.value)) # Adiciona ao texto da variavel "p_texto" apenas o que for numero.
        p_texto = p_texto[:3]

        if porcentagem_preco_venda.value == "porcentagem": # Se a opção de cálculo for inserindo a porcentagem.
            if p_texto: # Se p_texto == True, ou seja, tem algo
                lucro = int(p_texto) / 100 # Trasforma em int e divide a porcentagem digitada por 100
                valor = custo * (1 + lucro) # Multiplica pelo preco de custo a porcentagem digitada.

            else: # Senão, apenas passa o preço de custo como preço de venda
                valor = custo

        else:  # Se a opção de cálculo for inserindo manualmente
            n_texto = "".join(filter(str.isdigit, campo_preco_venda.value)) # Adiciona ao texto da variavel "p_texto" apenas o que for numero.

            if n_texto: # Se p_texto == True, ou seja, tem algo
                valor = int(n_texto) / 100 # Converte para int e divide por 100 para conseguir os dois dígitos dos centavos.
            
            else: # Senão, apenas passa o preço de custo como preço de venda
                valor = custo

        # Formata com separador de milhar e decimal
        formatado = f"R$ {valor:,.2f}".replace(",", "v").replace(".", ",").replace("v", ".")
        campo_preco_venda.value = formatado
        page.update()

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

    porcentagem = ft.TextField(label= "Porcentagem de lucro:", bgcolor=ft.Colors.WHITE, width=610, visible=True, on_change=formatar_preco_venda)

    campo_preco_venda = ft.TextField( # Terminar a formatação deste campo
        label="Preço de Venda:",
        value="",
        width=120,
        on_change=formatar_preco_venda,
    )

    campo_quantidade = ft.TextField(
        label="Quantidade:",
        value="",
        width=100,
        on_change=formatar_quantidade,
    )

    campo_validade = ft.TextField(
        label="Validade:",
        value="",
        width=120,
        on_change=formatar_validade,
    )

    def handle_change(e):
        # Atualiza o TextField com a data selecionada formatada
        data_formatada = e.control.value.strftime('%d/%m/%Y')
        campo_validade.value = data_formatada
        campo_validade.update()
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

    selecionar_data = ft.IconButton(icon=ft.Icons.CALENDAR_MONTH, on_click=abrir_datepicker, icon_color=ft.Colors.BLACK)







    # Função para buscar o cliente:
    def buscar_cliente(e):
        texto = e.control.value.lower().strip()

        tabela_estoque.rows.clear()

        for i, produto in enumerate(produtos):
            # Botão para editar as informações:
            botao_editar = ft.IconButton(
                icon=ft.Icons.EDIT,
                on_click=lambda e, index=i: editar(index), # Quando for clicado: passa o valor de i par ao parâmetro index da função editar e chama a função editar.
                style=ft.ButtonStyle(color="#507656"), # Cor do botão.
            )

            if texto in produto["nome"].lower() or texto in produto["codigo"].lower():
                tabela_estoque.rows.append(
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(produto["codigo"], size=14)), # Busca o valor atráves do nome no dicionário da função adicionar produto.
                            ft.DataCell(ft.Text(produto["nome"], size=14)),
                            ft.DataCell(ft.Text(produto["preco_custo"], size=14)),
                            ft.DataCell(ft.Text(produto["preco_venda"], size=14)),
                            ft.DataCell(ft.Text(produto["quantidade"], size=14)),
                            ft.DataCell(ft.Text(produto["validade"], size=14)),
                            ft.DataCell(botao_editar),
                        ],
                    ),
                )

        page.update()


    # Campo para busca de clientes:
    campo_buscar = ft.TextField(label="Buscar Produto:", hint_text="Código de Barras ou Nome", width=300, on_change=buscar_cliente)







    # Popup de erro caso algum campo esteja em branco:
    erro = ft.AlertDialog(
        title=ft.Text("Erro!", weight="bold"),

        content=ft.Container(
            content=ft.Container(
                content=ft.Text("Todos os campos devem estar preenchidos!", size=16, color="#9B3E3E"),
                width=300,
                height=50,
            ),
        ),

        actions=[
            ft.FilledButton(
                content=ft.Text("Ok", size=16), 
                style=ft.ButtonStyle(bgcolor="#507656", color=ft.Colors.WHITE), 
                on_click=fechar_erro
            ),
        ],

        actions_alignment=ft.MainAxisAlignment.CENTER,
        bgcolor=ft.Colors.WHITE,
    )







    # Variável para localzar o dado que será editado:
    index_editado = 0

    botao_salvar = ft.TextButton(
        content=ft.Text("Salvar", size=16),
        style=ft.ButtonStyle(bgcolor="#507656", color=ft.Colors.WHITE),
        on_click=lambda e: salvar(index_editado, campo_codigo_barras, campo_nome_produto, campo_preco_custo, campo_preco_venda, campo_quantidade, campo_validade)
    )

    botao_cancelar = ft.TextButton(
        content=ft.Text("Cancelar", size=16),
        style=ft.ButtonStyle(color="#9B3E3E"),
        on_click=cancelar,
    )


    # Janela de editar os dados do produto:
    janela_editar = ft.AlertDialog(
        title=ft.Text("Editar", weight="bold", text_align=ft.TextAlign.CENTER),

        content=ft.Container(
            content=ft.Column(
                controls=[
                    ft.ResponsiveRow(
                        controls=[
                            ft.Container(
                                content=campo_codigo_barras,
                                col={"xs":12, "sm":10, "md":6, "lg":5},
                            ),

                            ft.Container(
                                content=campo_nome_produto,
                                col={"xs":12, "sm":10, "md":6, "lg":5},
                            ),
                        ],

                        alignment=ft.MainAxisAlignment.CENTER,
                    ),

                    ft.ResponsiveRow(
                        controls=[
                            ft.Container(
                                content=campo_quantidade,
                                col={"xs":12, "sm":10, "md":6, "lg":5},
                            ),

                            ft.Container(
                                content=campo_validade,
                                col={"xs":10, "sm":9, "md":5, "lg":4},
                            ),

                            ft.Container(
                                content=selecionar_data,
                                col={"xs": 2, "sm": 1, "md":1},
                            ),
                        ],

                        alignment=ft.MainAxisAlignment.CENTER,
                    ),

                    ft.ResponsiveRow(
                        controls=[
                            ft.Container(
                                content=campo_preco_custo,
                                col={"xs":12, "sm":10, "md":6, "lg":5},
                            ),

                            ft.Container(
                                content=campo_preco_venda,
                                col={"xs":12, "sm":10, "md":6, "lg":5},
                            ),
                        ],

                        alignment=ft.MainAxisAlignment.CENTER,
                    ),

                    ft.ResponsiveRow(
                        controls=[
                            ft.Container(
                                content=porcentagem_preco_venda,
                                col={"xs":3, "sm":3, "md":3, "lg":3},
                            ),

                            ft.Container(
                                content=porcentagem,
                                col={"xs":9, "sm":9, "md":6, "lg":5},
                            ),
                        ],

                        alignment=ft.MainAxisAlignment.CENTER,
                    ),

                    ft.ResponsiveRow(
                        controls=[
                            ft.Container(
                                content=botao_cancelar,
                                col={"xs": 12, "sm":5, "md":4, "lg":3},
                            ),

                            ft.Container(
                                content=botao_salvar,
                                col={"xs": 12, "sm":5, "md":4, "lg":3},
                            ),
                        ],

                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                ],

                alignment=ft.MainAxisAlignment.CENTER,
            ),

            width=600,
            height=300,
        ),

        bgcolor=ft.Colors.WHITE,
        modal=True,
        alignment=ft.alignment.center,
        actions_alignment=ft.MainAxisAlignment.CENTER,
    )








    # Container que conterá a tabela de clientes (Ajudará a viabilizar algumas funções como o scroll e fixar o título no topo da tabela)
    container_tabela = ft.Container(
        content=ft.Column(
            [tabela_estoque],
            scroll=ft.ScrollMode.AUTO # Habilita o scroll automaticamente quando a altura máxima é atingida.
        ),

        expand=True,
        border=ft.border.all(2, color="#765070"),
        border_radius=10,
    )







    # Tela de estoque:
    layout = ft.Container(
        content=ft.Column(
            [
                ft.Text("Produtos Cadastrados", size=30, weight="bold"),

                ft.ResponsiveRow(
                    controls=[
                        ft.Container(
                            content=campo_buscar,
                            col={"xs":12, "sm":12, "md":6, "lg":4},
                        ),
                    ],

                    alignment=ft.MainAxisAlignment.CENTER,
                ),

                container_tabela,
            ],
            spacing=10,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),

        expand=True,
        bgcolor=ft.Colors.WHITE,
        margin=0,
        padding=20,
        border_radius=15,
        alignment=ft.alignment.center,
    )

    return layout
    