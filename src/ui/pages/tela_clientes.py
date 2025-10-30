import flet as ft

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

            if cliente.get("editando", False):
                campo_nome = ft.TextField(label="Nome:", value=cliente["nome"], width=200)

                
                campo_numero = ft.TextField(label="Número:", value=cliente["numero"], width=200, on_change=formatar_numero)

                global campo_cpf_cnpj # Campo global genérico para receber CPF ou CNPJ.

                # Se o tamanho da informação guardada na chave "cpf_cnpj" da lista de clientes for igual a 11 (tamanho de um cpf com sua formatação):
                if len(cliente["cpf_cnpj"]) == 14:
                    campo_cpf_cnpj = ft.TextField(label="CPF:", value=cliente["cpf_cnpj"], width=200, on_change=formatar_cpf)

                # Se o tamanho da informação guardada na chave "cpf_cnpj" da lista de clientes for igual a 18 (tamanho de um cnpj com sua formatação):
                elif len(cliente["cpf_cnpj"]) == 18:
                    campo_cpf_cnpj = ft.TextField(label="CNPJ:", value=cliente["cpf_cnpj"], width=200, on_change=formatar_cnpj)

                # Botão para salvar as alterações:
                botao_salvar = ft.TextButton(
                    text="Salvar",
                    on_click=lambda e, index=i: salvar(index, campo_nome, campo_numero, campo_cpf_cnpj),
                    style=ft.ButtonStyle(color="#507656"),
                )

                # Botão para cancelar a edição:
                botao_cancelar = ft.TextButton(
                    text="Cancelar",
                    on_click=lambda e, index=i: cancelar(index),
                    style=ft.ButtonStyle(color="#9B3E3E"),
                )

                tabela_clientes.rows.append( # Cria uma nova linha na tabela
                    ft.DataRow( # Cada linha/row (neste caso DataRow por ser a linha de uma tabela) é feita de várias células (DataCell), uma para cada coluna.
                        cells=[
                            ft.DataCell(campo_nome), # Adiciona os campos já preenchidos para que as informações ejam alteradas.
                            ft.DataCell(campo_numero),
                            ft.DataCell(campo_cpf_cnpj),
                            ft.DataCell(ft.Row([botao_salvar, botao_cancelar])),
                        ],
                    ),
                )

            else:
                # Botão para editar as informações:
                botao_editar = ft.TextButton(
                    content=ft.Text("Editar", size=16), # Texto escrito no botão
                    on_click=lambda e, index=i: editar(index), # Quando for clicado: passa o valor de i par ao parâmetro index da função editar e chama a função editar.
                    style=ft.ButtonStyle(color="#507656"), # Cor do texto.
                )

                # Botão para remover clientes da lista:
                botao_excluir = ft.TextButton(
                    content=ft.Text("Excluir", size=16), # Texto escrito no botão
                    on_click=lambda e, index=i: excluir(index), # Quando for clicado: passa o valor de i par ao parâmetro index da função editar e chama a função excluir.
                    style=ft.ButtonStyle(color="#9B3E3E"), # Cor do texto.
                )

                tabela_clientes.rows.append( # Cria uma nova linha na tabela
                    ft.DataRow( # Cada linha/row (neste caso DataRow por ser a linha de uma tabela) é feita de várias células (DataCell), uma para cada coluna.
                        cells = [
                            ft.DataCell(ft.Text(cliente["nome"], size=16)), # Busca o valor atráves do nome no dicionário da função adicionar produto.
                            ft.DataCell(ft.Text(cliente["numero"], size=16)),
                            ft.DataCell(ft.Text(cliente["cpf_cnpj"], size=16)),
                            ft.DataCell(ft.Row([botao_editar, botao_excluir])),
                            
                        ]
                    )
                )

        page.update()

    atualizar()



    # FUNÇÕES DE EDIÇÃO DA TABELA:

    # Função para editar os dados do cliente:
    def editar(index): # Recebe o index em que os dados estão localizados na lista de clientes.
        clientes[index]["editando"] = True # Muda o valor de editando para True.
        atualizar() # Atualiza a tabela.

    # Função para excluir os dados do cliente:
    def excluir(index): # Recebe o index em que os dados estão localizados na lista de clientes.
        if index < 0:
            return
        
        else:
            clientes.pop(index) # Exclui os dados que estão no index passado.
            atualizar() # Atualiza a tabela.

    # Função que salvará as alterações:
    def salvar(index, campo_nome, campo_numero, campo_cpf_cnpj): # Receberá o index e os campos onde serão inseridas as novas informações.
        clientes[index]["nome"] = campo_nome.value # Muda o valor da chave "nome" no index passado.
        clientes[index]["numero"] = campo_numero.value # Muda o valor da chave "numero" no index passado.
        clientes[index]["cpf_cnpj"] = campo_cpf_cnpj.value # Muda o valor da chave "cpf_cnpj" no index passado.
        clientes[index]["editando"] = False # Muda o valor da chave "editando" no index passado.
        atualizar() # Atualiza a tabela.

    # Função que cancelará qualquer alteração feita
    def cancelar(index): # Recebe o index dos dados do cliente.
        clientes[index]["editando"] = False # Apenas muda o valor da chave "editando" do index passado, para falso.
        atualizar() # atualiza a tabela.



    # FUNÇÕES DE FORMATAÇÃO:
    def formatar_cpf(e):
        texto = "".join(filter(str.isdigit, e.control.value))
        texto = texto[:11]

        formatado = ""

        if len(texto) > 0:
            formatado += texto[:3]
        if len(texto) > 3:
            formatado += "." + texto[3:6]
        if len(texto) > 6:
            formatado += "." + texto[6:9]
        if len(texto) > 9:
            formatado += "-" + texto[9:11]

        campo_cpf_cnpj.value = formatado
        page.update()

    def formatar_cnpj(e):
        texto = "".join(filter(str.isdigit, e.control.value))
        texto[:14]

        formatado = ""

        if len(texto) > 0:
            formatado += texto[:2]
        if len(texto) > 2:
            formatado += "." + texto[2:5]
        if len(texto) > 5:
            formatado += "." + texto[5:8]
        if len(texto) > 8:
            formatado += "/" + texto[8:12]
        if len(texto) > 12:
            formatado += "-" + texto[12:14]

        campo_cpf_cnpj.value = formatado
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

    return ft.Container(
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
