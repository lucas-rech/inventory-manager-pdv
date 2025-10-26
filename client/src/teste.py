import flet as ft

def main(page: ft.Page):
    def formatar_cpf(e):
        # Remove tudo que não for número
        texto = ''.join(filter(str.isdigit, e.control.value))

        # Limita a 11 dígitos
        texto = texto[:11]

        # Adiciona a máscara
        formatado = ""
        if len(texto) > 0:
            formatado = texto[:3]
        if len(texto) > 3:
            formatado += "." + texto[3:6]
        if len(texto) > 6:
            formatado += "." + texto[6:9]
        if len(texto) > 9:
            formatado += "-" + texto[9:11]

        # Atualiza o campo sem disparar o evento novamente
        cpf_field.value = formatado
        page.update()

    cpf_field = ft.TextField(
        label="CPF",
        width=250,
        on_change=formatar_cpf,
        keyboard_type=ft.KeyboardType.NUMBER,
    )

    page.add(cpf_field)

ft.app(target=main)


