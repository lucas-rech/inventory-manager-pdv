import flet as ft
import asyncio
from ui.components.botoes.botao_adicionar import criar_botao_adicionar
from ui.components.botoes.botao_finalizar import criar_botao_finalizar

def criar_tela_pdv(resumo_compra, produtos, page, header, conteudo_completo, voltar_venda_inicio):
    # Função que permitirá apenas números no campo de código:
    def formatar_codigo(e):
        texto = "".join(filter(str.isdigit, e.control.value)) # Apenas junte a string do que está sendo digitado o que for número.
        codigo.value = texto # Atualiza o campo enquanto o usuário digita.
        page.update() # Atualiza a tela


    codigo = ft.TextField(label="Código:", width=630, bgcolor=ft.Colors.WHITE, border=ft.border.all(1, color="#765070"), on_change=formatar_codigo)

    tabela_resumo_venda = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Código", weight="bold")),
            ft.DataColumn(ft.Text("Produto", weight="bold")),
            ft.DataColumn(ft.Text("Preço", weight="bold")),
            ft.DataColumn(ft.Text("Quantidade", weight="bold")),
            ft.DataColumn(ft.Text("Subtotal", weight="bold")),
        ],
        rows=[],
    )

    # Função que irá formatar o preco de venda para float novamente sem a formatação contábil para que não dê TypeError, já que o preco_venda está armazenado como string na lista de produtos:
    def formatar_preco_venda(pvenda):
        valor_pvenda = pvenda.replace("R$", "").replace(".", "").replace(",", ".") # Retira o cifrão e muda as vírgulas para o padrão de pontos.
        return valor_pvenda # Retorna o valor bruto, sem formatação nenhuma.

    def get_informacoes_produto(codigo):
        for c in produtos:
            if c["codigo"] == codigo:
                formatar_preco_venda(c["preco_venda"])
                return {
                    "codigo": c["codigo"],
                    "nome": c["nome"],
                    "preco_venda": float(formatar_preco_venda(c["preco_venda"])),
                    "quantidade": 1,
                }
        return None

    total = 0
    texto_total = ft.Text(value=f"Total: R$ {total:.2f}", weight="bold", size=40)

    def atualizar(e):
        nonlocal total # nonlocal se refere ao total declarado acima
        produto_encontrado = get_informacoes_produto(codigo.value)
        if not produto_encontrado: # Se não encontrar o produto não retorna nada e para a função aqui.
            return

        resumo_compra.append(produto_encontrado)
        tabela_resumo_venda.rows.clear()
        total = 0

        for p in resumo_compra:
            subtotal = p["preco_venda"] * p["quantidade"]
            total += subtotal
            tabela_resumo_venda.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(value=p["codigo"])),
                        ft.DataCell(ft.Text(p["nome"])),
                        ft.DataCell(ft.Text(p["preco_venda"])),
                        ft.DataCell(ft.Text(p["quantidade"])),
                        ft.DataCell(ft.Text(f"{subtotal:.2f}")),
                    ],
                )
            )

        texto_total.value = f"Total: R$ {total:.2f}"
        codigo.value = ""
        codigo.focus()
        page.update()

    botao_adicionar = criar_botao_adicionar(atualizar)

    # 🔹 Área da tabela limitada (com scroll)
    area_tabela = ft.Container(
        content=ft.Column(
            [
                ft.Text("Resumo da Compra", size=24, weight="bold"),
                tabela_resumo_venda
            ],
            spacing=20,
            scroll=ft.ScrollMode.AUTO,
        ),
        width=750,  # Define o tamanho máximo da tabela
        expand=True,
        padding=20,
        border=ft.border.all(1, color="#765070"),
        border_radius=10,
    )

    # 🔹 Campo total fixo
    total_compra = ft.Container(
        content=texto_total,
        bgcolor="#85A289",
        padding=ft.padding.all(15),
        border_radius=13,
        alignment=ft.alignment.center_right,
        width=400,
        height=100,
    )

    tela_finalizar_compra = criar_tela_finalizar_compra(area_tabela, texto_total, page, voltar_venda_inicio, resumo_compra) # Cirando a tela de finalizar compra
    
    def finalizar_compra(e): # Atualização do conteúdo para a tela de finaizar compra
        conteudo_completo.controls.clear() # Limpa tudo
        header.content.value = "Finalizar Compra" # Atualiza o header
        conteudo_completo.controls.append(header) # Adiciona ele na página
        conteudo_completo.controls.append(tela_finalizar_compra) # Adiciona a tela de finaliar compra

        page.update() # Atualiza a página para mostrar as alterações

    botao_finalizar_compra = criar_botao_finalizar(finalizar_compra)

    # 🔹 Layout principal com Stack (mantém o total fixo)
    layout = ft.Container(
            ft.Stack(
            controls=[
                ft.Row(
                    [
                        ft.Column(
                            [
                                ft.Row([codigo, botao_adicionar]),
                                area_tabela,  # à esquerda
                                ft.Row([botao_finalizar_compra], width=750, alignment=ft.MainAxisAlignment.END),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        ),

                        ft.Image(src="src/assets/Logo_semfundo.png", expand=True)  
                    ],
                    expand=True,
                ),
                ft.Container(
                    content=total_compra,
                    right=30,   # canto inferior direito
                    bottom=30,
                ),
            ],
            expand=True,
        ),

        expand=True, 
        bgcolor=ft.Colors.WHITE,
        padding=20,
        border_radius=13,
    )

    return layout

def criar_tela_finalizar_compra(area_tabela, texto_total, page, voltar_venda_inicio, resumo_compra): # Aqui será inserido a tabela com o resumo da compra, já formatada.
    # QR code: 
    qr_code = ft.Image(src="src/assets/qr-code.png", width=200, height=200) # Imagem do qrcode.
    transacao_aceita = ft.Icon( # Icone de transação validada
        name=ft.Icons.CHECK_CIRCLE,
        color="#507656",
        size=40,
        visible=False,
    )

    container_qr_code = ft.Container( # Container onde ficarão a imagem do qrcode e o icone de validação.
        content=ft.Column(
            controls=[
                ft.Row([qr_code], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([transacao_aceita], alignment=ft.MainAxisAlignment.CENTER),
            ],

            alignment=ft.MainAxisAlignment.CENTER,
        ),

        alignment=ft.alignment.center,
        bgcolor="#E8E3DE",
        width=250,
        height=300,
        border_radius=10,
        visible=False,
    )

    campo_valor_recebido = ft.TextField(label="Valor Recebido: ", width=300) # Campo que receberá a quantida de dinheiro dado pelo cliente.

    # Ações que serão executadas dentro da mini-janela:
    # Confirmar valor recebido:
    def confirmar(e):
        calcular_troco(campo_valor_recebido)
        page.close(layout_valor)
        page.update()

    # Cancelar ação:
    def cancelar(e):
        page.close(layout_valor)
        page.update()


    # Janela que irá ser aberta ao selecionar o método de pagamento "Dinheiro":
    layout_valor = ft.AlertDialog( # Cria um alert dialog que é a mini-janela ou popup.
        content=ft.Container( # O content da janela será um container que abrangerá tudo que estiver dentro.
            content=campo_valor_recebido, # O conteudo do container será um text field.
            width=400, # Largura do container
            height=100, # Altura do container
        ),

        modal=True, # Desabilita a interação do usuário com qualquer elemento fora da mini-janela.
        title=ft.Text("Valor Recebido"),
        actions=[ # Ações da janela: 
            ft.TextButton("Cancelar", on_click=cancelar), # Botão para cancelar
            ft.ElevatedButton("Confirmar", on_click=confirmar), # Botão para confirmar.
        ],

        actions_alignment=ft.MainAxisAlignment.END,
    )

    

    # Estou fazendo uma cópia do campo de total para evitar conflitos.
    novo_total_compra = ft.Container(
        content=texto_total,
        bgcolor="#85A289",
        padding=ft.padding.all(15),
        border_radius=13,
        alignment=ft.alignment.center,
        width=750,
        height=100,
    )

    # Texto com o troco total:
    total_troco = 0 # Variável para calcular o troco
    texto_troco = ft.Text(value=f"Troco: R${total_troco}", weight="bold", size=40)

    # Recalculando o total para utilizar no cálculo do troco:
    def calcular_total(resumo_compra):
        valor_total = 0
        for p in resumo_compra:
            valor_total += p["preco_venda"] * p["quantidade"]
        return valor_total

    # Função que calculará o troco:
    def calcular_troco(valor_recebido):
        v = valor_recebido.value
        total = calcular_total()
        nonlocal total_troco
        print(total_troco)
        total_troco = float(v) - total
        texto_troco.value = f"Troco: R${total_troco}"
        page.update()

    # Container onde ficará o troco que será necessário retornar ao cliente:
    container_troco = ft.Container(
        content=texto_troco,
        width=750,
        height=100,
        visible=False,
        bgcolor="#507656",
        border_radius=10,
        alignment=ft.alignment.center_right,
    )

    # escolha conforme o método de pagamento
    async def escolha_pagamento(e): # Define a função como assíncrona para evitar que a interface congele. (async)
        if e.control.value == "pix":
            container_troco.visible = False
            container_qr_code.visible = True
            page.update() # atualiza a UI de forma assíncrona, permitindo que outras tarefas continuem rodando enquanto a tela é atualizada.

            await asyncio.sleep(3) # Mesmo que o sleep porém de forma assíncrona. SEMPRE UTILIZAR ASYNC AO INVÉS DO SLEEP!  
            transacao_aceita.visible = True
            page.update()

        if e.control.value == "dinheiro":
            container_qr_code.visible = False # Esconde o container com o qr code
            transacao_aceita.visible = False # Esconde o sinal de validação da transação
            container_troco.visible = True # Deixa o campo que mostrará o campo com o troco necessário visível.
            page.open(layout_valor)
            page.update()
        
        if e.control.value == "débito":
            pass
        if e.control.value == "crédito":
            pass

    # Menu de seleção da forma de pagamento:
    menu_forma_pagamento = ft.Container(
        ft.RadioGroup(
            content=ft.Column(
                [
                    ft.Radio(label="💠 Pix", value="pix"), # O value será util para capturar a forma de pagamento selecionada, para que possa ser utilizada posteriormente.
                    ft.Radio(label="💵 Dinheiro", value="dinheiro"),
                    ft.Radio(label="💳 Débito", value="débito"),
                    ft.Radio(label="💳 Crédito", value="crédito"),
                ],
                spacing=10,
            ),
            on_change=lambda e: page.run_task(escolha_pagamento, e), # Criamos uma função anônima (lambda) que recebe o evento "e" como parâmetro "e", quando o evento on_change é disparado, ela executa de forma assíncrona a função escolha_pagamento(e) usando asyncio.create_task().

            value=None, # O valor inicial é nulo, nenhuma opção selecionada
        ),

        width=250,
        height=180,
        border=ft.border.all(1, "#765070"),
        border_radius=10,
    )

    botao_finalizar = criar_botao_finalizar(voltar_venda_inicio)
    botao_finalizar.width = 250

    layout = ft.Container(
        ft.Row(
            [
                ft.Column([area_tabela, novo_total_compra, container_troco], alignment=ft.MainAxisAlignment.START),
                ft.Column([menu_forma_pagamento, botao_finalizar, container_qr_code], alignment=ft.MainAxisAlignment.START),
            ],

            spacing=10,
            alignment=ft.MainAxisAlignment.CENTER,
        ),

        bgcolor=ft.Colors.WHITE,
        expand=True,
        padding=20,
        border_radius=13,
    )

    return layout
