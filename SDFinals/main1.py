import flet as ft

class Main:
    def main(page:ft.Page):
        def container(align: ft.CrossAxisAlignment):
            mainfont = '#fbbf69'
            backfont = '#fff5cc'
            passw = ft.TextField(
                label = "Password",
                password = True,
                can_reveal_password = True,
                border_color = mainfont,
                border_radius = 100,
                width = 230.4,
                color = mainfont,
                cursor_color = mainfont,
                text_align = 'left',
                suffix_style = ft.ButtonStyle(
                    color = backfont
                )
            )
            
            ft.Container(
                bgcolor = backfont,
                border_radius = 50,
                height = 617.6,
                width = 288,
                margin = 0,
                content =
                    ft.Column([
                            ft.Image(
                                src = "images/logo.png",
                                width = 200,
                                height = 200
                            ),
                            ft.Divider(
                                height = 50,
                                color = 'transparent'
                            ),
                            passw,
                            ft.Text("Forgot password? E-mail sdgroup5@gmail.com",
                                size = 7,
                                color = mainfont
                            ),
                            ft.FilledButton(
                                text = "Log In",
                                style = ft.ButtonStyle(
                                    bgcolor = mainfont,
                                    color = backfont
                                ),
                                on_click = login
                            )
                        ],
                        height = 400,
                        width = 230.4,
                        alignment = ft.MainAxisAlignment.CENTER,
                        horizontal_alignment = align      
                    )
            )
    
        def login(e):
            v = ft.Text()
            v.value = Main.passw.value
            print(v.value)
        
        page.add(
            ft.Row([
                container(ft.CrossAxisAlignment.CENTER)],
                alignment = ft.MainAxisAlignment.START 
            )
        )
        
        page.update()
        
    ft.app(
        target = main,
        assets_dir = "images"
    )