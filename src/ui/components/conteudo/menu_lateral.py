from flet import *

# Menu lateral:
def criar_menu_lateral(on_change):
    return NavigationRail(
        selected_index=0,
        bgcolor="#D2DEEC",
        label_type=NavigationRailLabelType.ALL,
        group_alignment=-1.0,  # Itens principais no topo
        on_change=on_change, # o valor atribuído é o parâmetro da função "criar_menu_lateral" (não é uma redundância).
        destinations=[
            NavigationRailDestination(icon=Icons.ADD, label="Cadastrar"),
            NavigationRailDestination(icon=Icons.LIST, label="Estoque"),
            NavigationRailDestination(icon=Icons.PERSON, label="Clientes"),
        ],
        
        # 👇 Ícone fixo no final da barra
        trailing=Container(
            content=IconButton(
                icon=Icons.SETTINGS,
                tooltip="Configurações",
                on_click=lambda e: print("Configurações clicadas!"),
            ),
            alignment=alignment.bottom_center,
            padding=10,
        ),
    )