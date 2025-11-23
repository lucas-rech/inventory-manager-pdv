import flet as ft
from validate_docbr import CPF,CNPJ
import re
import asyncio

def criar_tela_clientes(clientes, page):
    tabela_clientes = ft.DataTable(
        columns=[ # Define as 2 colunas que terão dados (Nome, Número)
            ft.DataColumn(ft.Text("Nome", size=18)),
            ft.DataColumn(ft.Text("Número de Telefone", size=18)),
            ft.DataColumn(ft.Text("CPF / CNPJ", size=18)),
            ft.DataColumn(ft.Text("Ações", size=18))
        ],

        rows = [], # As linhas começam vazias, sem nenhum cliente cadstrado.

        width=1300,
    )


    # Função que adicionará itens à tabela de estoque:
    def atualizar():
        tabela_clientes.rows.clear() # Limpa todas as tabelas anteriores para atualizar tudo do zero.

        for i, cliente in enumerate(clientes):# Para cada indice e item que está naquele índice, da lista "clientes".

            # Botão para editar as informações:
            botao_editar = ft.IconButton(
                icon=ft.Icons.EDIT,
                on_click=lambda e, index=i: editar(index), # Quando for clicado: passa o valor de i par ao parâmetro index da função editar e chama a função editar.
                style=ft.ButtonStyle(color="#507656"), # Cor do texto.
            )



            tabela_clientes.rows.append( # Cria uma nova linha na tabela
                ft.DataRow( # Cada linha/row (neste caso DataRow por ser a linha de uma tabela) é feita de várias células (DataCell), uma para cada coluna.
                    cells = [
                        ft.DataCell(ft.Text(cliente["nome"], size=16)), # Busca o valor atráves do nome no dicionário da função adicionar produto.
                        ft.DataCell(ft.Text(cliente["numero"], size=16)),
                        ft.DataCell(ft.Text(cliente["cpf_cnpj"], size=16)),
                        ft.DataCell(botao_editar),
                        
                    ]
                )
            )

        page.update()

    atualizar()


    # FUNÇÕES DE EDIÇÃO DA TABELA:
    index_editado = 0
    
    # Função para editar os dados do cliente:
    def editar(index): # Recebe o index em que os dados estão localizados na lista de clientes.

        nonlocal index_editado
        index_editado = index

        campo_nome.value = clientes[index]["nome"]
        campo_numero.value = clientes[index]["numero"]

        page.open(janela_editar)
        atualizar() # Atualiza a tabela.

    # Função que salvará as alterações:
    def salvar(index, campo_nome, campo_numero): # Receberá o index e os campos onde serão inseridas as novas informações.

        if not campo_nome.value or not campo_numero.value:
            page.open(erro) # Mensagem de erro
            page.update()
            
        else:
            clientes[index]["nome"] = campo_nome.value # Muda o valor da chave "nome" no index passado.
            clientes[index]["numero"] = campo_numero.value # Muda o valor da chave "numero" no index passado.

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

    # Função que cancelará qualquer alteração feita
    def cancelar(e):
        page.close(janela_editar)
        page.update()
        
        atualizar() # atualiza a tabela.






    # FUNÇÕES DE FORMATAÇÃO:
    def formatar_nome(e):
        texto = e.control.value
        texto = texto[:80]

        # Substitui os espaços duplicados digitados no campo_nome por apenas 1.
        campo_nome.value = re.sub(r"\s{2,}", " ", texto) # Se qualquer espaço aparecer 2 ou mais vezes ({2,}), substitui por um apenas (" ").
        page.update()


    def formatar_numero(e):
        texto = "".join(filter(str.isdigit, e.control.value))
        texto = texto[:11]

        formatado = ""

        if len(texto) > 0:
            formatado += f"({texto[:2]}) "
        if len(texto) > 2:
            formatado += texto[2:7]
        if len(texto) > 7:
            formatado += "-" + texto[7:11]

        campo_numero.value = formatado
        page.update()






    # Função para buscar o cliente:
    def buscar_cliente(e):
        texto = e.control.value.lower().strip()

        tabela_clientes.rows.clear()

        for i, cliente in enumerate(clientes):
            # Botão para editar as informações:
            botao_editar = ft.IconButton(
                icon=ft.Icons.EDIT,
                on_click=lambda e, index=i: editar(index), # Quando for clicado: passa o valor de i par ao parâmetro index da função editar e chama a função editar.
                style=ft.ButtonStyle(color="#507656"), # Cor do botão.
            )

            if texto in cliente["nome"].lower() or texto in cliente["numero"].lower() or texto in cliente["cpf_cnpj"].lower():
                tabela_clientes.rows.append(
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(cliente["nome"])),
                            ft.DataCell(ft.Text(cliente["numero"])),
                            ft.DataCell(ft.Text(cliente["cpf_cnpj"])),
                            ft.DataCell(botao_editar),
                        ],
                    ),
                )

        page.update()


    # Campo para busca de clientes:
    campo_buscar = ft.TextField(label="Buscar Cliente:", hint_text="Nome, Número, CPF/CNPJ", width=300, on_change=buscar_cliente)






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
            ft.FilledButton(content=ft.Text("Ok", size=16), style=ft.ButtonStyle(bgcolor="#507656", color=ft.Colors.WHITE), on_click=fechar_erro),
        ],

        actions_alignment=ft.MainAxisAlignment.CENTER,
        bgcolor=ft.Colors.WHITE,
    )

    # Botão para salvar as alterações:
    botao_salvar = ft.TextButton(
        content=ft.Text("Salvar", size=16),
        on_click=lambda e: salvar(index_editado, campo_nome, campo_numero),
        style=ft.ButtonStyle(bgcolor="#507656", color=ft.Colors.WHITE),
    )

    # Botão para cancelar a edição:
    botao_cancelar = ft.TextButton(
        content=ft.Text("Cancelar", size=16),
        on_click=cancelar,
        style=ft.ButtonStyle(color="#9B3E3E"),
    )

    campo_nome = ft.TextField(label="Nome:", value="", width=200, on_change=formatar_nome)

    campo_numero = ft.TextField(label="Telefone:", value="", width=200, on_change=formatar_numero)

    janela_editar = ft.AlertDialog(
        title=ft.Text("Editar", weight="bold", text_align=ft.TextAlign.CENTER),

        content=ft.Container(
            content=ft.Column(
                controls=[
                    ft.ResponsiveRow(
                        controls=[
                            ft.Container(
                                content=campo_nome,
                                col={"xs": 12, "sm":12, "md":10, "lg":10},
                            ),
                        ],

                        alignment=ft.MainAxisAlignment.CENTER,
                    ),

                    ft.ResponsiveRow(
                        controls=[
                            ft.Container(
                                content=campo_numero,
                                col={"xs": 12, "sm":12, "md":10, "lg":10},
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
                spacing=10,
            ),

            width=500,
            height=200,
        ),

        alignment=ft.alignment.center,
        modal=True,
        bgcolor=ft.Colors.WHITE,
    )
    






    # Container que conterá a tabela de clientes (Ajudará a viabilizar algumas funções como o scroll e fixar o título no topo da tabela)
    container_tabela = ft.Container(
        content=ft.Column(
            [tabela_clientes],
            scroll=ft.ScrollMode.AUTO, # Habilita o scroll automaticamente quando a altura máxima é atingida.
        ),

        expand=True, # Altura máxima
        border=ft.border.all(2, color="#765070"),
        border_radius=10
    )






    layout = ft.Container(
        content=ft.Column(
            [
                ft.Text("Clientes Cadastrados", size=30, weight="bold"),

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
