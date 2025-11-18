import flet as ft
import asyncio
import re

def main(page: ft.Page):

    page.title = "Teste de Clientes"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.AUTO

    # Lista de clientes para teste
    clientes = [
        {"nome": "Bruno Silva", "numero": "(11) 98765-4321", "cpf_cnpj": "123.456.789-00"},
        {"nome": "Bruno Borges", "numero": "(11) 91234-1111", "cpf_cnpj": "987.654.321-00"},
        {"nome": "Ana Clara", "numero": "(11) 99888-7777", "cpf_cnpj": "321.321.321-99"},
        {"nome": "Carlos Santos", "numero": "(21) 95555-5555", "cpf_cnpj": "111.222.333-44"},
        {"nome": "Bruno Silveira", "numero": "(19) 97777-9999", "cpf_cnpj": "555.666.777-88"},
    ]

    # --------------------------------------------------------------
    # Tabela
    # --------------------------------------------------------------
    tabela_clientes = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Nome")),
            ft.DataColumn(ft.Text("Telefone")),
            ft.DataColumn(ft.Text("CPF/CNPJ")),
        ],
        rows=[],
        width=800,
    )

    # Atualiza tabela completa
    def atualizar():
        tabela_clientes.rows.clear()
        for cliente in clientes:
            tabela_clientes.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(cliente["nome"])),
                        ft.DataCell(ft.Text(cliente["numero"])),
                        ft.DataCell(ft.Text(cliente["cpf_cnpj"])),
                    ]
                )
            )
        page.update()

    # --------------------------------------------------------------
    # FILTRAGEM
    # --------------------------------------------------------------
    def filtrar(texto_busca):
        texto = texto_busca.lower().strip()

        tabela_clientes.rows.clear()

        for cliente in clientes:
            if texto in cliente["nome"].lower() \
               or texto in cliente["numero"].lower() \
               or texto in cliente["cpf_cnpj"].lower():

                tabela_clientes.rows.append(
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(cliente["nome"])),
                            ft.DataCell(ft.Text(cliente["numero"])),
                            ft.DataCell(ft.Text(cliente["cpf_cnpj"])),
                        ]
                    )
                )

        page.update()

    # Campo de busca
    campo_busca = ft.TextField(
        label="Buscar cliente...",
        width=300,
        on_change=lambda e: filtrar(e.control.value)
    )

    atualizar()

    # --------------------------------------------------------------
    # Layout Final
    # --------------------------------------------------------------
    layout = ft.Column(
        [
            ft.Text("Clientes Cadastrados", size=26, weight="bold"),
            campo_busca,
            tabela_clientes,
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20
    )

    page.add(layout)


# Roda o app
ft.app(target=main)
