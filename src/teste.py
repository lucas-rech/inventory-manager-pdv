import flet as ft  # Importa a biblioteca Flet

def main(page: ft.Page):
    page.title = "Tabela simples com editar e excluir"

    # Lista que armazenará os dados (cada item será um dicionário)
    dados = []

    # Campos de entrada para adicionar novos itens
    nome = ft.TextField(label="Nome", width=200)
    numero = ft.TextField(label="Número", width=150)

    # Cria a tabela inicial (sem linhas)
    tabela = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Nome")),
            ft.DataColumn(ft.Text("Número")),
            ft.DataColumn(ft.Text("Ações")),
        ],
        rows=[],
    )

    # --- FUNÇÕES ---

    # Atualiza a tabela exibida na tela
    def atualizar():
        tabela.rows.clear()  # Remove todas as linhas atuais

        # Percorre a lista de dados e cria uma linha para cada item
        for i, item in enumerate(dados):
            if item.get("editando", False):  # Se estiver no modo edição
                # Campos para editar o nome e o número
                campo_nome = ft.TextField(value=item["nome"], width=120)
                campo_num = ft.TextField(value=item["numero"], width=100)

                # Botão para salvar as alterações
                btn_salvar = ft.ElevatedButton(
                    text="Salvar",
                    on_click=lambda e, i=i, n=campo_nome, nu=campo_num: salvar(i, n, nu)
                )

                # Botão para cancelar a edição
                btn_cancelar = ft.TextButton(
                    text="Cancelar",
                    on_click=lambda e, i=i: cancelar(i)
                )

                # Linha com campos de edição
                tabela.rows.append(
                    ft.DataRow(
                        cells=[
                            ft.DataCell(campo_nome),
                            ft.DataCell(campo_num),
                            ft.DataCell(ft.Row([btn_salvar, btn_cancelar]))
                        ]
                    )
                )

            else:  # Modo normal (somente leitura)
                # Botão de editar
                btn_editar = ft.TextButton(
                    text="Editar",
                    on_click=lambda e, i=i: editar(i)
                )

                # Botão de excluir
                btn_excluir = ft.TextButton(
                    text="Excluir",
                    on_click=lambda e, i=i: excluir(i),
                    style=ft.ButtonStyle(color=ft.Colors.RED)
                )

                # Linha normal da tabela
                tabela.rows.append(
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(item["nome"])),
                            ft.DataCell(ft.Text(item["numero"])),
                            ft.DataCell(ft.Row([btn_editar, btn_excluir]))
                        ]
                    )
                )

        page.update()  # Atualiza a interface

    # Adiciona um novo item à lista
    def adicionar(e):
        if nome.value and numero.value:  # Verifica se os campos não estão vazios
            dados.append({"nome": nome.value, "numero": numero.value, "editando": False})
            nome.value = ""
            numero.value = ""
            atualizar()  # Recria a tabela

    # Coloca o item em modo de edição
    def editar(index):
        dados[index]["editando"] = True
        atualizar()

    # Salva as alterações feitas na linha
    def salvar(index, campo_nome, campo_num):
        dados[index]["nome"] = campo_nome.value
        dados[index]["numero"] = campo_num.value
        dados[index]["editando"] = False
        atualizar()

    # Cancela o modo de edição (sem salvar)
    def cancelar(index):
        dados[index]["editando"] = False
        atualizar()

    # Exclui o item da lista
    def excluir(index):
        dados.pop(index)
        atualizar()

    # Botão principal para adicionar novos dados
    botao_add = ft.ElevatedButton(text="Adicionar", on_click=adicionar)

    # Adiciona tudo na página
    page.add(
        ft.Column(
            [
                ft.Row([nome, numero, botao_add]),  # Linha superior de entrada
                tabela,  # Tabela principal
            ]
        )
    )

ft.app(target=main)
