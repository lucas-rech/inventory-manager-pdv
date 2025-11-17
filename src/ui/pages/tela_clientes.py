import flet as ft
from validate_docbr import CPF,CNPJ

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

    # Função para excluir os dados do cliente:
    def excluir(index): # Recebe o index em que os dados estão localizados na lista de clientes.
        if index < 0:
            return
        
        else:
            clientes.pop(index) # Exclui os dados que estão no index passado.
            atualizar() # Atualiza a tabela.

    # Função que salvará as alterações:
    def salvar(index, campo_nome, campo_numero): # Receberá o index e os campos onde serão inseridas as novas informações.

        clientes[index]["nome"] = campo_nome.value # Muda o valor da chave "nome" no index passado.
        clientes[index]["numero"] = campo_numero.value # Muda o valor da chave "numero" no index passado.

        page.close(janela_editar)
        page.update()

        atualizar() # Atualiza a tabela.

    # Função que cancelará qualquer alteração feita
    def cancelar(index): # Recebe o index dos dados do cliente.
        page.close(janela_editar)
        page.update()
        
        atualizar() # atualiza a tabela.






    # FUNÇÕES DE FORMATAÇÃO:
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






    # Botão para salvar as alterações:
    botao_salvar = ft.TextButton(
        text="Salvar",
        on_click=lambda e, index=index_editado: salvar(index, campo_nome, campo_numero),
        style=ft.ButtonStyle(color="#507656"),
    )

    # Botão para cancelar a edição:
    botao_cancelar = ft.TextButton(
        text="Cancelar",
        on_click=lambda e, index=index_editado: cancelar(index),
        style=ft.ButtonStyle(color="#9B3E3E"),
    )


    campo_nome = ft.TextField(label="Nome:", value="", width=200)

    campo_numero = ft.TextField(label="Número:", value="", width=200, on_change=formatar_numero)

    janela_editar = ft.AlertDialog(
        content=ft.Container(
            content=ft.Column(
                controls=[
                    ft.ResponsiveRow(
                        controls=[
                            ft.Container(
                                content=ft.Text("Editar Dados", size=20, weight="bold"),
                                alignment=ft.alignment.center,
                            )
                        ]
                    ),

                    ft.ResponsiveRow(
                        controls=[
                            ft.Container(
                                content=campo_nome,
                                col={"xs": 12, "sm":9, "md":6, "lg":6},
                            ),
                        ],

                        alignment=ft.MainAxisAlignment.CENTER,
                    ),

                    ft.ResponsiveRow(
                        controls=[
                            ft.Container(
                                content=campo_numero,
                                col={"xs": 12, "sm":9, "md":6, "lg":6},
                            ),
                        ],

                        alignment=ft.MainAxisAlignment.CENTER,
                    ),

                    ft.ResponsiveRow(
                        controls=[
                            ft.Container(
                                content=botao_cancelar,
                                col={"xs": 12, "sm":4, "md":3, "lg":2},
                            ),

                            ft.Container(
                                content=botao_salvar,
                                col={"xs": 12, "sm":4, "md":3, "lg":2},
                            ),
                        ],

                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                ],

                alignment=ft.MainAxisAlignment.CENTER,
                spacing=10,
            ),

            width=530,
            height=400,
        ),

        alignment=ft.alignment.center,
        modal=True,
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
