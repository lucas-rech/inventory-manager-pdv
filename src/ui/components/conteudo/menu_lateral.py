import flet as ft

# Menu lateral:
def criar_menu_lateral(on_change):
    return ft.NavigationRail(
        selected_index=0,
        bgcolor="#85a289",
        label_type=ft.NavigationRailLabelType.ALL,
        group_alignment=-1.0,  # Itens principais no topo
        on_change=on_change, # o valor atribuído é o parâmetro da função "criar_menu_lateral" (não é uma redundância).
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.SHOPPING_BAG, label="Venda"),
            ft.NavigationRailDestination(icon=ft.Icons.ADD, label="Cadastrar"),
            ft.NavigationRailDestination(icon=ft.Icons.LIST, label="Estoque"),
            ft.NavigationRailDestination(icon=ft.Icons.PERSON, label="Clientes"),
        ],
        
        # 👇 Ícone fixo no final da barra
        trailing=ft.Container(
            content=ft.IconButton(
                icon=ft.Icons.SETTINGS,
                tooltip="Configurações",
                on_click=lambda e: print("Configurações clicadas!"),
                icon_color="#e8e3de"
            ),
            alignment=ft.alignment.bottom_center,
            padding=10,
        ),
    )