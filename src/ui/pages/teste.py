import flet as ft

def main(page: ft.Page):
    # Função para capturar a mudança
    def selecionar_pagamento(e):
        print("Selecionado:", grupo_pagamento.value)

    # RadioGroup para seleção única
    grupo_pagamento = ft.RadioGroup(
        content=ft.Column(
            [
                ft.Radio(label="Dinheiro", value="dinheiro"),
                ft.Radio(label="Pix", value="pix"),
                ft.Radio(label="Débito", value="debito"),
                ft.Radio(label="Crédito", value="credito"),
            ]
        ),
        value="dinheiro",  # valor inicial
        on_change=selecionar_pagamento,
    )

    page.add(grupo_pagamento)

ft.app(target=main)
