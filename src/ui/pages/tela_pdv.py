import flet as ft
import asyncio
from ui.components.botoes.botao_adicionar import criar_botao_adicionar
from ui.components.botoes.botao_finalizar import criar_botao_finalizar

def criar_tela_pdv(resumo_compra, produtos, page, header, conteudo_completo, voltar_venda_inicio):
    # Função que permitirá apenas números no campo de código:
    def formatar_codigo(e):
        texto = "".join(filter(str.isdigit, e.control.value)) # Apenas junte a string do que está sendo digitado o que for número.
        texto = texto[:13]

        codigo.value = texto # Atualiza o campo enquanto o usuário digita.
        page.update() # Atualiza a tela

    def formatar_quantidade(e):
        texto = "".join(filter(str.isdigit, e.control.value))
        texto = texto[:5]
        quantidade.value = texto
        page.update()

    erro_quantidade = ft.AlertDialog(
        content=ft.Container(
            content=ft.Column()
        )
    )


    codigo = ft.TextField(label="Código:", width=630, bgcolor=ft.Colors.WHITE, border=ft.border.all(1, color="#765070"), on_change=formatar_codigo)

    quantidade = ft.TextField(label="Quantidade:", width=630, bgcolor=ft.Colors.WHITE, border=ft.border.all(1, color="#765070"), on_change=formatar_quantidade, value="1")

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
    def desformatar_preco_venda(pvenda):
        valor_pvenda = pvenda.replace("R$", "").replace(".", "").replace(",", ".") # Retira o cifrão e muda as vírgulas para o padrão de pontos.
        return valor_pvenda # Retorna o valor bruto, sem formatação nenhuma.
    
    def formatar_preco_venda(pvenda):
        formatado = f"R$ {pvenda:,.2f}".replace(".", "v").replace(",", ".").replace("v", ",") # Adiciona à variável de retorno.

        return formatado # Retorno a variável.

    def get_informacoes_produto(codigo):
        for c in produtos:
            if c["codigo"] == codigo:

                return {
                    "codigo": c["codigo"],
                    "nome": c["nome"],
                    "preco_venda": float(desformatar_preco_venda(c["preco_venda"])),
                    "quantidade": int(quantidade.value),
                }
        return None
    
    # Função para formatar o total da compra para a formataçõa contábil brasileira:
    def formatar_total(valor):
        v = valor
        total_formatado = f"R$ {v:,.2f}".replace(".", "v").replace(",", ".").replace("v", ",")
        return total_formatado

    total = 0
    texto_total = ft.Text(value=f"Total: R$ {total:,.2f}", weight="bold", size=40)

    def formatar_subtotal(subtotal):
        formatado = f"R$ {subtotal:,.2f}".replace(".", "v").replace(",", ".").replace("v", ",")

        return formatado


    # Função que atualiza a tabela de resumo de venda:
    def atualizar(e):
        nonlocal total # nonlocal se refere ao total declarado acima

        if not quantidade.value: # Se não for passada quantidade, o valor padrão passado é 1.
            quantidade.value = "1"

        produto_encontrado = get_informacoes_produto(codigo.value)

        if not produto_encontrado: # Se não encontrar o produto não retorna nada e para a função aqui.
            return

        resumo_compra.append(produto_encontrado)
        tabela_resumo_venda.rows.clear()
        total = 0
        subtotal = 0

        for p in resumo_compra:
            subtotal = p["preco_venda"] * p["quantidade"]

            total += subtotal
            tabela_resumo_venda.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(value=p["codigo"])),
                        ft.DataCell(ft.Text(p["nome"])),
                        ft.DataCell(ft.Text(formatar_preco_venda(p["preco_venda"]))),
                        ft.DataCell(ft.Text(p["quantidade"])),
                        ft.DataCell(ft.Text(formatar_subtotal(subtotal))),
                    ],
                )
            )

        texto_total.value = f"Total: {formatar_total(total)}"
        codigo.value = ""
        codigo.focus()
        page.update()

    botao_adicionar = ft.Container(
        content=ft.Text("Adicionar", color=ft.Colors.WHITE, size=20),
        bgcolor="#507656",
        width=110,
        height=100,
        ink=True,
        on_click=atualizar,
        alignment=ft.alignment.center,
        border_radius=10,
    )

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

    # Layout principal com Stack (mantém o total fixo)
    layout = ft.Container(
            ft.Stack(
            controls=[
                ft.Row(
                    [
                        ft.Column(
                            [
                                ft.Row(controls=[
                                    ft.Column([codigo, quantidade]),
                                    botao_adicionar,
                                ]),

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

    def formatar_valor_recebido(e):
        texto = "".join(filter(str.isdigit, e.control.value)) # Junte à string apenas o que for número 
        texto = texto[:13] # Limita o tamanho máximo para 13 caracteres

        if not texto:
            campo_valor_recebido.value = "R$ 0,00"
            page.update()
            return # O return está vazio aqui para quefuncione como um "Break" da função, ou seja para aqui.

        valor_texto = float(texto) / 100 # Altera o tipo da variável para float e divide por 100 para que comece preenchendo pela direita nos centavos.

        formatado = f"R$ {valor_texto:,.2f}".replace(".", "v").replace(",", ".").replace("v", ",") # Muda o que for "." para "v" temporariamente, o que for  "," por "." e o que for "v" para ",".

        campo_valor_recebido.value = formatado # Atualiza o que está sendo escrito coma formatação
        page.update() # Atualiza a página.
        

    campo_valor_recebido = ft.TextField(label="Valor Recebido: ", width=300, on_change=formatar_valor_recebido) # Campo que receberá a quantida de dinheiro dado pelo cliente.

    # Ações que serão executadas dentro da mini-janela:
    # Confirmar valor recebido:
    def confirmar(e):
        total = calcular_total(resumo_compra) # Recalculo o total para que eu possa usar depois.

        # Se o troco for menor que o total da compra:
        if float(campo_valor_recebido.value.replace("R$ ", "").replace(".", "").replace(",", ".")) < total:
            page.open(troco_errado) # Mensagem de erro
            page.update()
        
        else:
            calcular_troco(campo_valor_recebido)
            page.close(layout_valor)
            page.update()

    # Cancelar ação:
    def cancelar(e):
        page.close(layout_valor)
        campo_valor_recebido.value = ""
        page.update()

    def fechar_erro(e):
        page.close(troco_errado) # Abre o popup de erro.
        page.update() # Atualiza a interface primeiro.
        page.run_task(reabrir_valor) # Depois de atualizar dá run no próximo processo para evitar deadlock

    async def reabrir_valor():
        await asyncio.sleep(0.05) # Dá um tempo para a interface até executar o próximo processo para evitar deadlock.
        page.open(layout_valor) # Abre para o minijanela "layout_valor" para que o usuário insira o troco.
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
            ft.TextButton(content=ft.Text("Cancelar", size=16), on_click=cancelar, style=ft.ButtonStyle(color="#9B3E3E")), # Botão para cancelar
            ft.ElevatedButton(content=ft.Text("Confirmar", size=16), on_click=confirmar, color="#507656"), # Botão para confirmar.
        ],

        actions_alignment=ft.MainAxisAlignment.END,
        bgcolor="#E8E3DE",
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
    texto_troco = ft.Text(value=f"Troco: R${total_troco:.2f}", weight="bold", size=40)

    # Foramatando o troco para a formatação contábil brasileira:
    def formatar_troco(valor):
        v = valor 
        troco_formatado = f"R$ {v:,.2f}".replace(".", "v").replace(",", ".").replace("v", ",") # Precisa ser :,.2f pois assim ele adiciona uma vírgula para separar os milhares, senão ficaria apenas "1000.00"
        return troco_formatado

    # Recalculando o total para utilizar no cálculo do troco:
    def calcular_total(resumo_compra):
        valor_total = 0

        for p in resumo_compra:
            valor_total += p["preco_venda"] * p["quantidade"]

        return valor_total
    
    # Pup-up de erro caso o troco inserido seja menor que o total da compra:
    troco_errado = ft.AlertDialog(
        content=ft.Container(
            content=ft.Text("O valor recebido não pode ser menor que o total da compra!", size=16, color="#9B3E3E"),
            width=300,
            height=50,
        ),
        modal=True, # Desabilita qualquer ação fora do popup.
        title=ft.Text("Erro!", weight="bold"),
        actions=[
            ft.FilledButton(content=ft.Text("Ok", size=16), style=ft.ButtonStyle(bgcolor="#507656", color=ft.Colors.WHITE), on_click=fechar_erro),
        ],

        actions_alignment=ft.MainAxisAlignment.CENTER,
        bgcolor=ft.Colors.WHITE,
    )

    # Função que calculará o troco:
    def calcular_troco(valor_recebido):
        v = valor_recebido.value.replace("R$ ", "").replace(".", "").replace(",", ".")
        print(v)

        total = calcular_total(resumo_compra)

        nonlocal total_troco
        total_troco = float(v) - total

        texto_troco.value = f"Troco: {formatar_troco(total_troco)}"
        page.update()

    # Container onde ficará o troco que será necessário retornar ao cliente:
    container_troco = ft.Container(
        content=texto_troco,
        width=750,
        height=100,
        visible=False,
        bgcolor="#507656",
        border_radius=10,
        alignment=ft.alignment.center,
    )

    # Função caso pix seja a forma de pagamento selecionada:
    async def processsar_pix():
        container_troco.visible = False
        container_qr_code.visible = True
        transacao_aceita.visible = False    
        page.update() # atualiza a UI de forma assíncrona, permitindo que outras tarefas continuem rodando enquanto a tela é atualizada.

        await asyncio.sleep(3) # Mesmo que o sleep porém de forma assíncrona. SEMPRE UTILIZAR ASYNC AO INVÉS DO SLEEP!  

        transacao_aceita.visible = True
        page.update()

    task_pix = None # Variável para guardar o estado atual da forma de pagamento via pix.

    # Função caso débito seja a forma de pagamento selecionada:
    async def processar_debito():
        container_qr_code.visible = False
        container_troco.visible = False
        transacao_aceita.visible = False
        page.open(debito)
        page.update()

        await asyncio.sleep(3) # Mesmo que o sleep porém de forma assíncrona. SEMPRE UTILIZAR ASYNC AO INVÉS DO SLEEP!

        transacao_aceita.visible = True
        page.update() 

        await asyncio.sleep(2) # Mesmo que o sleep porém de forma assíncrona. SEMPRE UTILIZAR ASYNC AO INVÉS DO SLEEP!
        page.close(debito)
        page.update()

    task_debito = None
    imagem = ft.Image(src="src/assets/pagamento-cartao.jpg", width=200, height=130)

    # Definição do modal de débito:
    debito = ft.AlertDialog(
        content=ft.Container(
            ft.Column(
                controls=[
                    ft.Row([imagem], alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row([ft.Text("Aproxime ou insira o cartão na maquininha", size=20)], alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row([transacao_aceita], alignment=ft.MainAxisAlignment.CENTER),
                ], 
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            width=400,
            height=200,
        ),

        modal=True,
        title=ft.Text("Efetuar pagamento: DÉBITO"),
        bgcolor=ft.Colors.WHITE,
    )

    # Função caso crédito seja a forma de pagamento selecionada:
    async def processar_credito():
        container_qr_code.visible = False
        container_troco.visible = False
        transacao_aceita.visible = False
        page.open(credito)
        page.update()

        await asyncio.sleep(3) # Mesmo que o sleep porém de forma assíncrona. SEMPRE UTILIZAR ASYNC AO INVÉS DO SLEEP!
        
        transacao_aceita.visible = True
        page.update()

        await asyncio.sleep(2) # Mesmo que o sleep porém de forma assíncrona. SEMPRE UTILIZAR ASYNC AO INVÉS DO SLEEP!
        page.close(credito)
        page.update()

    task_credito = None

    credito = ft.AlertDialog(
        content=ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row([imagem], alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row([ft.Text("Aproxime ou insira o cartão na maquininha", size=20)], alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row([transacao_aceita], alignment=ft.MainAxisAlignment.CENTER),
                ],

                alignment=ft.MainAxisAlignment.CENTER,
            ),

            width=400,
            height=200,
        ),

        modal=True,
        title=ft.Text("Efetuar pagamento: CRÉDITO"),
        bgcolor=ft.Colors.WHITE,
    )

    # escolha conforme o método de pagamento
    async def escolha_pagamento(e): # Define a função como assíncrona para evitar que a interface congele. (async)
        nonlocal task_pix
        nonlocal task_debito
        nonlocal task_credito

        if task_pix and not task_pix.done(): # Cancelar taskpix em andamento, se estiver ativo mas não estiver terminada:
            task_pix.cancel() # Cancela o processo.
            await asyncio.sleep(0) # Libera o loop

        metodo = e.control.value # Método de pagamento escolhido

        if metodo == "pix":
            task_debito = None
            task_credito = None
            task_pix = asyncio.create_task(processsar_pix())

        elif metodo == "dinheiro":
            task_pix = None
            task_debito = None
            task_credito = None
            container_qr_code.visible = False # Esconde o container com o qr code
            transacao_aceita.visible = False # Esconde o sinal de validação da transação
            container_troco.visible = True # Deixa o campo que mostrará o campo com o troco necessário visível.
            page.open(layout_valor)
            campo_valor_recebido.focus()
            page.update()
        
        elif metodo == "débito":
            task_pix = None
            task_credito = None
            task_debito = asyncio.create_task(processar_debito())

        elif e.control.value == "crédito":
            task_debito = None
            task_pix = None
            task_credito = asyncio.create_task(processar_credito())

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

    popups = []

    def mostrar_popup(e):
        pb = ft.ProgressBar(width=200, value=0)

        popup = ft.Container(
            content=ft.Column(
                
            )
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
