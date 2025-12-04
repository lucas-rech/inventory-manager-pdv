import flet as ft
import re
import datetime
import asyncio
from ui.components.botoes.botao_adicionar import criar_botao_adicionar
import copy

# Função que irá criar a tela de estoque:
def criar_tela_estoque(produtos, page):
    index_produto_atual = None

    # Tabela dos itens em estoque:
    tabela_estoque = ft.DataTable(
        columns=[ # Define as 6 colunas que terão dados (Código, Nome, Preço de custo, Preço de venda, Quantidade e Validade)
            ft.DataColumn(ft.Text("Código de Barras", size=16)),
            ft.DataColumn(ft.Text("Nome", size=16)),
            ft.DataColumn(ft.Text("Preço de custo", size=16)),
            ft.DataColumn(ft.Text("Preço de venda", size=16)),
            ft.DataColumn(ft.Text("Quantidade", size=16)),
            ft.DataColumn(ft.Text("Ações", size=16))
        ],

        rows=[], # As linhas começam vazias, sem nenhum item em estoque.

        width=1500,
    )


    # Função calcular quantidade total, baseado na quantidade declarada nos lotes:
    def calcular_quantidade_total(produto):
    # Retorna a soma da quantidade de todos os lotes
        return sum(int(lote["quantidade"]) for lote in produto["lotes"])

    # Função que adicionará itens à tabela de estoque:
    def atualizar(): 
        tabela_estoque.rows.clear() # Limpa todas as tabelas anteriores para atualizar tudo do zero.

        for i, produto in enumerate(produtos): # Para cada indice da lista "produtos"
            botao_editar = ft.IconButton(
                icon=ft.Icons.EDIT,
                style=ft.ButtonStyle(color="#507656"), # Cor do botão.
                on_click=lambda e, index=i: editar_produto(index), # Quando for clicado: passa o valor de i par ao parâmetro index da função editar e chama a função editar.
            )

            botao_duplicar = ft.IconButton(
                icon=ft.Icons.COPY,
                style=ft.ButtonStyle(color="#507656"), # Cor do botão.
                on_click=lambda e, index=i: duplicar_produto(index), # Quando for clicado: passa o valor de i par ao parâmetro index da função editar e chama a função editar.
            )

            botao_lotes = ft.IconButton(
                icon=ft.Icons.ADD_BOX,
                style=ft.ButtonStyle(color="#507656"),
                on_click=lambda e, index=i: abrir_janela_lote(e, index),
            )
            
            tabela_estoque.rows.append( # Cria uma nova linha na tabela

                ft.DataRow( # Cada linha/row (neste caso DataRow por ser a linha de uma tabela) é feita de várias células (DataCell), uma para cada coluna.
                    cells=[
                        ft.DataCell(ft.Text(produto["codigo"], size=14)), # Busca o valor atráves do nome no dicionário da função adicionar produto.
                        ft.DataCell(ft.Text(produto["nome"], size=14)),
                        ft.DataCell(ft.Text(produto["preco_custo"], size=14)),
                        ft.DataCell(ft.Text(produto["preco_venda"], size=14)),
                        ft.DataCell(ft.Text(str(calcular_quantidade_total(produto)), size=14)),
                        ft.DataCell(ft.Row([botao_editar, botao_duplicar, botao_lotes])),
                    ]
                )
            ) 

        page.update() # Atualiza a página para mostrar as alterações.

    atualizar()







    # FUNÇÕES DE EDIÇÃO DA TABELA:
    # Função de editar dados da tabela:
    def editar_produto(index): # Recebe o index dos dados que serão editados.
        campo_codigo_barras.value = produtos[index]["codigo"]
        campo_nome_produto.value = produtos[index]["nome"]
        campo_preco_custo.value = produtos[index]["preco_custo"]
        campo_preco_venda.value = produtos[index]["preco_venda"]

        page.open(janela_editar) # Abre a janela de edição dos dados.

        nonlocal index_produto_editado
        index_produto_editado = index

        atualizar() # Atualiza a tabela.

    # Função de duplicar produtos:
    def duplicar_produto(index):
        produto_duplicado = {
            "codigo": produtos[index]["codigo"],
            "nome": produtos[index]["nome"],
            "preco_custo": produtos[index]["preco_custo"],
            "preco_venda": produtos[index]["preco_venda"],
            "quantidade": produtos[index]["quantidade"],
            "lotes": copy.deepcopy(produtos[index]["lotes"]),
        }

        produtos.insert(index + 1, produto_duplicado)
        atualizar()



    # Função de salvar os novos dados na tabela:
    def salvar(index, campo_codigo_barras, campo_nome_produto, campo_preco_custo, campo_preco_venda): # Recebe os campos que recebem as novas informações.
        if not campo_codigo_barras.value or not campo_nome_produto.value or not campo_preco_custo.value or not campo_preco_venda.value:
            page.open(erro) # Mensagem de erro
            page.update()

        else:
            produtos[index]["codigo"] = campo_codigo_barras.value # Muda o dado contido na chave codigo, no index passado.
            produtos[index]["nome"] = campo_nome_produto.value # Muda o dado contido na chave nome, no index passado.
            produtos[index]["preco_custo"] = campo_preco_custo.value # Muda o dado contido na chave preco_custo, no index passado.
            produtos[index]["preco_venda"] = campo_preco_venda.value # Muda o dado contido na chave preco_venda, no index passado.

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


    def abrir_janela_lote(e, index_produto):
        # capture explicitamente o produto atual para evitar leitura de variáveis mutáveis depois
        nonlocal index_produto_editado
        index_produto_editado = index_produto

        # atualiza o comportamento do botão "Adicionar" para abrir o diálogo com o índice correto
        # (botao_adicionar existe no escopo dos lotes; garantimos que ele use index_produto)
        botao_adicionar.on_click = lambda ev, ip=index_produto_editado: abrir_dados_lote(ev, ip)

        mostrar_lotes(index_produto)
        page.open(janela_lotes)
        page.update()









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
        e.control.value = texto
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

        e.control.value = formatado
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


    def handle_change(e):
        # Atualiza o TextField com a data selecionada formatada
        data_formatada = e.control.value.strftime('%d/%m/%Y')
        e.control.value = data_formatada
        e.control.update()
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







    # Função para buscar o produto:
    def buscar_produto(e):
        texto = e.control.value.lower().strip()

        tabela_estoque.rows.clear()

        for i, produto in enumerate(produtos):
            # Botão para editar as informações:
            botao_editar = ft.IconButton(
                icon=ft.Icons.EDIT,
                on_click=lambda e, index=i: editar_produto(index), # Quando for clicado: passa o valor de i par ao parâmetro index da função editar e chama a função editar.
                style=ft.ButtonStyle(color="#507656"), # Cor do botão.
            )

            # Botão para duplicar os produtos:
            botao_duplicar = ft.IconButton(
                icon=ft.Icons.COPY,
                style=ft.ButtonStyle(color="#507656"), # Cor do botão.
                on_click=lambda e, index=i: duplicar_produto(index), # Quando for clicado: passa o valor de i par ao parâmetro index da função editar e chama a função editar.
            )

            botao_lotes = ft.IconButton(
                icon=ft.Icons.ADD_BOX,
                style=ft.ButtonStyle(color="#507656"),
                on_click=lambda e, index=i: abrir_janela_lote(e, index),
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
                            ft.DataCell(ft.Row([botao_editar, botao_duplicar, botao_lotes])),
                        ],
                    ),
                )

        page.update()


    # Campo para busca de clientes:
    campo_buscar = ft.TextField(label="Buscar Produto:", hint_text="Código de Barras ou Nome", width=300, on_change=buscar_produto)







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
    index_produto_editado = 0

    botao_salvar = ft.TextButton(
        content=ft.Text("Salvar", size=16),
        style=ft.ButtonStyle(bgcolor="#507656", color=ft.Colors.WHITE),
        on_click=lambda e: salvar(index_produto_editado, campo_codigo_barras, campo_nome_produto, campo_preco_custo, campo_preco_venda)
    )

    botao_cancelar = ft.TextButton(
        content=ft.Text("Cancelar", size=16),
        style=ft.ButtonStyle(color="#9B3E3E"),
        on_click=cancelar,
    )


    # Mini-janelas:
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




    # --- LOTES ---

    index_lote_editado = 0

    header = ft.Container(
        content=ft.Text("Lotes Do Produto", color=ft.Colors.WHITE, size=25, weight="bold"),
        bgcolor="#507656",
        width=800,
        height=70,
        alignment=ft.alignment.center,
        border_radius=10,
    )


    async def reabrir_janela_lotes():
        await asyncio.sleep(0.05)
        page.open(janela_lotes)
        mostrar_lotes(index_produto_editado)
        page.update()


    # Função para a criação dos lotes:
    def criar_lote(e, index_produto):
        produto = produtos[index_produto]

        if not campo_quantidade_lote.value:
            novo_lote = {
                "numero_lote": campo_numero_lote.value,
                "data_fabricacao": campo_data_fabricacao.value,
                "data_validade": campo_data_validade.value,
                "quantidade": 0,
            }

        else:
            novo_lote = {
                "numero_lote": campo_numero_lote.value,
                "data_fabricacao": campo_data_fabricacao.value,
                "data_validade": campo_data_validade.value,
                "quantidade": campo_quantidade_lote.value,
            }

        produto["lotes"].append(novo_lote)

        for campo in [campo_numero_lote, campo_data_fabricacao, campo_data_validade, campo_quantidade_lote]:
            campo.value = ""

        page.close(janela_dados_lote)
        # Recarrega lotes com o índice CORRETO
        mostrar_lotes(index_produto)
        atualizar()
        page.run_task(reabrir_janela_lotes)
        page.update()


    # Função de editar os dados do lote:
    def editar_lote(index_produto, index_lote):
        produto = produtos[index_produto]
        lote = produto["lotes"][index_lote]

        campo_numero_lote.value = lote["numero_lote"]
        campo_data_fabricacao.value = lote["data_fabricacao"]
        campo_data_validade.value = lote["data_validade"]
        campo_quantidade_lote.value = lote["quantidade"]

        # salvar terá referência correta
        botao_salvar_lote.on_click = lambda e, ip=index_produto, il=index_lote: salvar_lote(ip, il)

        page.open(janela_edicao_lote)
        page.update()


    # Função de salvar os novos dados do lote na tabela:
    def salvar_lote(index_produto, index_lote):
        produto = produtos[index_produto]["lotes"][index_lote]

        produto["numero_lote"] = campo_numero_lote.value
        produto["data_fabricacao"] = campo_data_fabricacao.value
        produto["data_validade"] = campo_data_validade.value

        if not campo_quantidade_lote.value:
            produto["quantidade"] = 0

        else:
            produto["quantidade"] = campo_quantidade_lote.value

        for campo in [campo_numero_lote, campo_data_fabricacao, campo_data_validade, campo_quantidade_lote]:
            campo.value = ""

        page.close(janela_edicao_lote)
        mostrar_lotes(index_produto)
        atualizar()
        page.run_task(reabrir_janela_lotes)
        page.update()

    
    # Função de cancelar edição do lote:
    def cancelar_lote(index_produto):
        page.close(janela_dados_lote)
        mostrar_lotes(index_produto)
        page.run_task(reabrir_janela_lotes)
        page.update()


    # Função para duplicar lotes:
    def duplicar_lote(index_produto, index_lote):
        produto = produtos[index_produto]["lotes"]

        lote = produto[index_lote].copy()
        produto.insert(index_lote + 1, lote)

        mostrar_lotes(index_produto)
        atualizar()
        page.update()


    # Função para excluir lotes:
    def excluir_lote(index_produto, index_lote):
        produtos[index_produto]["lotes"].pop(index_lote)

        mostrar_lotes(index_produto)
        atualizar()
        page.update()
        
            

    def abrir_dados_lote(e, index_produto):
        botao_confirmar.on_click = lambda ev, ip=index_produto: criar_lote(ev, ip)

        # Limpa campos - SEM update()
        campo_numero_lote.value = ""
        campo_data_fabricacao.value = ""
        campo_data_validade.value = ""
        campo_quantidade_lote.value = ""

        page.open(janela_dados_lote)
        campo_numero_lote.focus()
        page.update()


    # Função para fechar a janela de listagem dos lotes:
    def fechar_janela_lote(e):
        page.close(janela_lotes)
        page.update()

    # Botão adicionar:
    botao_adicionar = criar_botao_adicionar(lambda e: abrir_dados_lote(e, index_produto_editado))

    botao_fechar = ft.ElevatedButton(
        bgcolor="#9B3E3E", 
        content=ft.Text("Fechar", size=16),
        color=ft.Colors.WHITE,
        on_click=fechar_janela_lote,
        height=50,
        width=125,
    )

    # Tabela com os lotes atrelados ao produto:
    tabela_lotes = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Número do Lote")),
            ft.DataColumn(ft.Text("Data de Fabricação")),
            ft.DataColumn(ft.Text("Data de Validade")),
            ft.DataColumn(ft.Text("Quantidade")),
            ft.DataColumn(ft.Text("Ações")),
        ],

        rows=[],

        width=850,
        height=450,
    )


    # Função para atualizar a tabela dos lotes:
    def mostrar_lotes(index_produto):
        tabela_lotes.rows.clear()
        produto = produtos[index_produto]

        for index_lote, lote in enumerate(produto["lotes"]):

            btn_editar = ft.IconButton(
                icon=ft.Icons.EDIT,
                style=ft.ButtonStyle(color="#507656"),
                on_click=lambda e, ip=index_produto, il=index_lote: editar_lote(ip, il),
            )

            btn_duplicar = ft.IconButton(
                icon=ft.Icons.COPY,
                style=ft.ButtonStyle(color="#507656"),
                on_click=lambda e, ip=index_produto, il=index_lote: duplicar_lote(ip, il),
            )

            btn_excluir = ft.IconButton(
                icon=ft.Icons.DELETE,
                style=ft.ButtonStyle(color="#9B3E3E"),
                on_click=lambda e, ip=index_produto, il=index_lote: excluir_lote(ip, il),
            )

            tabela_lotes.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(lote["numero_lote"])),
                        ft.DataCell(ft.Text(lote["data_fabricacao"])),
                        ft.DataCell(ft.Text(lote["data_validade"])),
                        ft.DataCell(ft.Text(lote["quantidade"])),
                        ft.DataCell(ft.Row([btn_editar, btn_duplicar, btn_excluir])),
                    ]
                )
            )

        page.update()


    # Container que conterá a tabela de lotes (Ajudará a viabilizar algumas funções como o scroll e fixar o título no topo da tabela)
    container_tabela_lotes = ft.Container(
        content=ft.Column(
            [tabela_lotes],
            scroll=ft.ScrollMode.AUTO # Habilita o scroll automaticamente quando a altura máxima é atingida.
        ),

        expand=True,
        border=ft.border.all(2, color="#765070"),
        border_radius=10,
    )


    # Janela para criação de lotes:
    janela_lotes = ft.AlertDialog(
        title=header,

        content=ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row([botao_fechar, botao_adicionar], alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row([container_tabela_lotes], alignment=ft.MainAxisAlignment.CENTER),
                ],
            ),

            width=900,
            height=500,
        ),

        bgcolor=ft.Colors.WHITE,
        alignment=ft.alignment.center,
    )

    # Campos para inserção dos dados do lote:
    campo_numero_lote = ft.TextField(label="Número do Lote", expand=True, on_change=formatar_codigo_barras)
    campo_data_fabricacao = ft.TextField(label="Data de Fabricação:", bgcolor=ft.Colors.WHITE, expand=True, on_change=formatar_validade)
    campo_data_validade = ft.TextField(label="Data de Validade:", bgcolor=ft.Colors.WHITE, expand=True, on_change=formatar_validade)
    campo_quantidade_lote = ft.TextField(label="Quantidade:", expand=True, on_change=formatar_quantidade)

    botao_confirmar = ft.ElevatedButton(
        content= ft.Text(value="Confirmar", size=16),
        bgcolor= "#507656",
        color= ft.Colors.WHITE,
        # on_click será substituído dinamicamente em abrir_dados_lote
        on_click=lambda e: None,
        height=50,
        width=110,
    )

    # Janela para inserção dos dados de criação do lote:
    janela_dados_lote = ft.AlertDialog(
        title=ft.Container(
            content=ft.Text("Insira os Dados do Lote", color=ft.Colors.WHITE, size=20),
            bgcolor="#507656",
            border_radius=8,
            height=50,
            alignment=ft.alignment.center,
        ),

        content=ft.Container(
            content=ft.Column(
                controls=[
                    ft.Container(
                        content=campo_numero_lote,
                    ),

                    ft.Container(
                        content=campo_data_fabricacao,
                    ),

                    ft.Container(
                        content=campo_data_validade
                    ),

                    ft.Container(
                        content=campo_quantidade_lote,
                    ),
                ],

                spacing=20
            ),

            width=300,
            height=280,
            padding=10,
        ),

        actions=[
            botao_confirmar,
        ],

        bgcolor=ft.Colors.WHITE,
        alignment=ft.alignment.center,
        actions_alignment=ft.MainAxisAlignment.CENTER,
        modal=True,
    )







    
    botao_salvar_lote = ft.TextButton(
        content=ft.Text("Salvar", size=16),
        style=ft.ButtonStyle(bgcolor="#507656", color=ft.Colors.WHITE),
        on_click=lambda e: None,  # será sobrescrito por editar_lote
    )

    botao_cancelar_lote = ft.TextButton(
        content=ft.Text("Cancelar", size=16),
        style=ft.ButtonStyle(color="#9B3E3E"),
        on_click=lambda e, ip=index_produto_editado: cancelar_lote(ip),
    )


    # Janela para inserção dos dados de edição do lote:
    janela_edicao_lote = ft.AlertDialog(
        title=ft.Container(
            content=ft.Text("Insira os Novos Dados do Lote", color=ft.Colors.WHITE, size=20),
            bgcolor="#507656",
            border_radius=8,
            height=50,
            alignment=ft.alignment.center,
        ),

        content=ft.Container(
            content=ft.Column(
                controls=[
                    ft.Container(
                        content=campo_numero_lote,
                    ),

                    ft.Container(
                        content=campo_data_fabricacao,
                    ),

                    ft.Container(
                        content=campo_data_validade
                    ),

                    ft.Container(
                        content=campo_quantidade_lote,
                    ),
                ],

                spacing=20
            ),

            width=300,
            height=280,
            padding=10,
        ),

        actions=[
            botao_cancelar_lote,
            botao_salvar_lote,
        ],

        bgcolor=ft.Colors.WHITE,
        alignment=ft.alignment.center,
        actions_alignment=ft.MainAxisAlignment.CENTER,
        modal=True,
    )



    # Container que conterá a tabela de estoque (Ajudará a viabilizar algumas funções como o scroll e fixar o título no topo da tabela)
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
    