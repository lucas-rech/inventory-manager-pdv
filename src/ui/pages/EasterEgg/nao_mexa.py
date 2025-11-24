from turtle import shape
from flet import *

def grid(proporcao):
    grid = GridView(
        expand=1,
        runs_count=3,
        child_aspect_ratio=proporcao,
        spacing=5,
        run_spacing=5,
        controls=[
            Image(
                src=f"https://picsum.photos/150?{num}",
                fit=ImageFit.COVER,
            )
            for num in range(60)
        ]
    )

    return grid

def easter_egg():

    header = Container(
        content=ResponsiveRow(
            columns=12,
            controls=[
                Container(
                    col={"xs": 12, "sm": 4},
                    content=Image(src="src/assets/foto.png", 
                        border_radius=border_radius.all(100),
                        fit=ImageFit.CONTAIN,
                        width=200,
                        height=200,
                        ),
                    bgcolor=Colors.BLACK,
                    shape=BoxShape.CIRCLE,
                    height=200,
                ),
                Container(
                    col={"xs": 12, "sm": 8},
                    content=ResponsiveRow(
                        controls=[
                            Row(
                                col=11,
                                controls=[
                                    Text(value="Casal_do_ano",
                                         color=Colors.BLACK,
                                         size=24,
                                         ),
                                    Icon(
                                        name=Icons.VERIFIED,
                                        color=Colors.BLUE_500,
                                        size=20,
                                    )
                                ]
                            ),
                            Icon(
                                col=1,
                                name=Icons.MORE_HORIZ,
                                color=Colors.BLACK,
                                size=20,
                            ),
                            Container(
                                col=4,
                                bgcolor=Colors.BLUE_500,
                                border_radius=border_radius.all(10),
                                padding=padding.symmetric(vertical=5, horizontal=10), alignment=alignment.center,
                                content=Text(
                                    value="Seguir",
                                    color=Colors.WHITE,
                                    size=14,
                                    weight=FontWeight.BOLD,
                                )
                            ),
                            Container(
                                col=6,
                                bgcolor=Colors.GREY_300,
                                border_radius=border_radius.all(10),
                                padding=padding.symmetric(vertical=5, horizontal=10),
                                alignment=alignment.center,
                                content=Text(
                                    value="Enviar Mesagem",
                                    weight=FontWeight.BOLD,
                                    color=Colors.BLACK,
                                    size=14,
                                    max_lines=1,
                                    overflow=TextOverflow.ELLIPSIS,
                                ),
                            ),
                            Text(
                                col={"xs": 12, "sm": 4},
                                spans=[
                                    TextSpan(
                                        text="150 ",
                                        style=TextStyle(
                                            weight=FontWeight.BOLD,
                                            color=Colors.BLACK,
                                        ),
                                    ),
                                    TextSpan(
                                        text="publicações",
                                        style=TextStyle(
                                            color=Colors.BLACK,
                                        ),
                                    ),
                                ]
                            ),
                            Text(
                                col={"xs": 12, "sm": 4},
                                spans=[
                                    TextSpan(
                                        text="10 ",
                                        style=TextStyle(
                                            weight=FontWeight.BOLD,
                                            color=Colors.BLACK,
                                        ),
                                    ),
                                    TextSpan(
                                        text="seguindo",
                                        style=TextStyle(
                                            color=Colors.BLACK,
                                        )
                                    ),
                                ]
                            ),
                            Text(
                                col={"xs": 12, "sm": 4},
                                spans=[
                                    TextSpan(
                                        text="200 ",
                                        style=TextStyle(
                                            weight=FontWeight.BOLD,
                                            color=Colors.BLACK,
                                        ),
                                    ),
                                    TextSpan(
                                        text="seguidores",
                                        style=TextStyle(
                                            color=Colors.BLACK,
                                        ),
                                    )
                                ]
                            ),
                            Text(
                                col=12,
                                value="Programaçao 3",
                                color=Colors.BLACK,
                                weight=FontWeight.BOLD
                            ),
                            Text(
                                col=12,
                                color=Colors.BLACK,
                                spans=[
                                    TextSpan(text="Parabéns! Você encontrou a zoeira interna dos desenvolvedores!\n"),
                                    TextSpan(text="Neste momento, você atingiu o nível master de tester!\n"),
                                    TextSpan(text="Seja bem-vindo ao mundo BugDoor!\n"),
                                    TextSpan(text="Vivemos nosso romance às escondidas\n"),
                                    TextSpan(text= "🔗 Link do Vídeo do nosso casamento",
                                        url="https://rlv.zcache.com.br/adesivo_quadrado_gorilla_finger-r2da3e881de9f42d298c0eeecfca328f6_zg2qg7_644.webp?rlvnet=1",
                                        style=TextStyle(
                                            color=Colors.BLUE
                                        )
                                    )
                                ]
                            ),
                            Text(
                                spans=[
                                    TextSpan(
                                        text="Seguido por ",
                                        style=TextStyle(
                                            color=Colors.BLACK,
                                        ),
                                    ),
                                    TextSpan(
                                        text="filipe_zaffonatto",
                                        style=TextStyle(
                                            color=Colors.BLACK,
                                            weight=FontWeight.BOLD
                                        ),
                                    ),
                                    TextSpan(
                                        text=", ",
                                        style=TextStyle(
                                            color=Colors.BLACK,
                                        ),
                                    ),
                                    TextSpan(
                                        text="larissa_da_leve ",
                                        style=TextStyle(
                                            color=Colors.BLACK,
                                            weight=FontWeight.BOLD,
                                        )
                                    ),
                                    TextSpan(
                                        text="e ",
                                        style=TextStyle(
                                            color=Colors.BLACK,
                                        )
                                    ),
                                    TextSpan(
                                        text="outras 24 pessoas",
                                        style=TextStyle(
                                            color=Colors.BLACK,
                                            weight=FontWeight.BOLD
                                        )
                                    )
                                ]
                            ),
                        ]
                    )
                )
            ]
        )
    )

    stories = Container(
        content=Row(
            scroll=ScrollMode.HIDDEN,
            controls=[
                Image(
                    src=f"https://picsum.photos/150?{num}",
                    border_radius=border_radius.all(100),
                    width=100,
                )
                    for num in range(15)
            ]
        )
    )

    divider = Divider()

    tab = Container(
        content=Tabs(
            divider_color=Colors.WHITE,
            label_color=Colors.BLACK,
            unselected_label_color=Colors.GREY_500,
            indicator_color=Colors.WHITE,
            selected_index=0,
            animation_duration=300,
            scrollable=False,
            tabs=[
                Tab(
                    text="Publicações",
                    icon=Icons.GRID_ON_OUTLINED,
                    content=Container(
                        content=grid(1.0)
                    )
                ),
                Tab(
                    text="Reels",
                    icon=Icons.VIDEO_COLLECTION_OUTLINED,
                    content=Container(
                        content=grid(9 / 16)
                    )
                ),
                Tab(
                    text="Salvos",
                    icon=Icons.BOOKMARK_OUTLINE,
                    content=Container(
                        content=grid(16 / 9)
                    )
                )
            ]
        )
    )


    layout = Container(
        content=Column(
            controls=[
                header,
                stories,
                divider,
                tab,
            ]
        )
    )

    return layout