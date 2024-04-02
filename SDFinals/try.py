#modules
import flet as ft
import time
import os
import mysql.connector
from dotenv import load_dotenv

#global variables
mainfont = '#fbbf69'
backfont = '#fff5cc'

#loads .env file that contains the database credentials
load_dotenv()

#loads .env data into python file
db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")
db_port = os.getenv("DB_PORT")

#initialize database     
db = mysql.connector.connect(
    host = db_host, 
    user = db_user, 
    password = db_password, 
    database = db_name, 
    port = int(db_port)
)

cursor = db.cursor()

#global variables
mainfont = '#fbbf69'
backfont = '#fff5cc'

def main(page: ft.Page):
    
    ###control variables
    page.fonts = {
        "Roboto Static": "https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap"
    }
    
    image = ft.Image(
        src = f"https://lh3.googleusercontent.com/a/ACg8ocIAY8jNypsDprgge-kJJF_wjgGu8MZw4mKBIo9IOlfu1Igmq5T4UeEA-YWAD94p-QS014v7Ay2Gk1EMzzU71iiyeg=s360-c-no",
        height = 300,
        width = 300
    )
    
    top_img = ft.Image(
        src = f"https://lh3.googleusercontent.com/a/ACg8ocIAY8jNypsDprgge-kJJF_wjgGu8MZw4mKBIo9IOlfu1Igmq5T4UeEA-YWAD94p-QS014v7Ay2Gk1EMzzU71iiyeg=s360-c-no",
        height = 50,
        width = 50
    )
    
    filledbtn = ft.FilledButton(
        "Log In",
        style = ft.ButtonStyle(
                bgcolor = mainfont,
        ),
        on_click = lambda e: login(e)
    )
    
    passw = ft.TextField(
        label = "Password",
        password = True,
        can_reveal_password = True,
        content_padding = ft.padding.all(20),
        border_color = mainfont,
        border_radius = 100,
        width = 300,
        color = mainfont,
        cursor_color = mainfont,
        text_align = 'left',
        cursor_radius = 10,
        #error_text: //lalabas pag may error?
        label_style = ft.TextStyle(
            color = mainfont,
            weight = ft.FontWeight.BOLD
        ),
        on_submit = lambda e: login(e)
    )
    
    dlg_modal = ft.AlertDialog(
        modal = True,
        content = ft.Text(
            "Wrong password. Please try again.",
            color = mainfont
            ),
        actions = [
            ft.TextButton(
                "Ok",
                on_click = lambda e: close_dlg(e),
                style = ft.ButtonStyle(
                    color = backfont,
                    bgcolor = mainfont
                )
            )
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )
    
    dlg_modal_noinp = ft.AlertDialog(
        modal = True,
        content = ft.Text(
            "Please input field.",
            color = mainfont
        ),
        actions = [
            ft.TextButton(
                "Ok",
                on_click = lambda e: close_dlg(e),
                style = ft.ButtonStyle(
                    bgcolor = mainfont,
                    color = backfont
                )
            )
        ],
        actions_alignment = ft.MainAxisAlignment.END,
    )
    
    drawer = ft.NavigationDrawer(
        controls = [
            ft.Container(height = 12),
            ft.NavigationDrawerDestination(
                label = "Item 1",
                icon = ft.icons.DOOR_BACK_DOOR_OUTLINED,
                selected_icon_content = ft.Icon(ft.icons.DOOR_BACK_DOOR),
            ),
            ft.Divider(thickness = 2),
            ft.NavigationDrawerDestination(
                icon_content = ft.Icon(ft.icons.MAIL_OUTLINED),
                label = "Item 2",
                selected_icon = ft.icons.MAIL,
            ),
            ft.NavigationDrawerDestination(
                icon_content=ft.Icon(ft.icons.PHONE_OUTLINED),
                label="Item 3",
                selected_icon=ft.icons.PHONE,
            )
        ]
    )

    ###function

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.SafeArea(
                        minimum = 5,
                        content = ft.Column(
                            alignment = 'center',
                            spacing = 0,
                            controls = [
                                ft.Row(
                                    alignment = 'end',
                                    controls = [
                                        ft.IconButton(
                                            scale = 0.85,
                                            icon = ft.icons.DARK_MODE_ROUNDED,
                                            icon_color = mainfont,
                                            on_click = lambda e: toggle_theme(e)
                                        )
                                    ]
                                ),
                                ft.Row(
                                    alignment = 'center',
                                    controls = [
                                        image
                                    ]
                                ),
                                ft.Row(
                                    alignment = 'center',
                                    controls = [
                                        passw
                                    ]
                                ),
                                ft.Divider(height = 20, color = 'transparent'),
                                ft.Row(
                                    alignment = 'center',
                                    controls = [
                                        filledbtn
                                    ]
                                ),
                                ft.Divider(height = 210, color = 'transparent'),
                                ft.Row(
                                    alignment = 'center',
                                    controls = [
                                        ft.Text(
                                            "Forgot password? Contact sd.group5@gmail.com",
                                            size = 12,
                                            weight = ft.FontWeight.BOLD,
                                            color = mainfont,
                                            text_align = 'center'
                                        )
                                    ]
                                ),
                                ft.Row(
                                    alignment = 'center',
                                    controls = [
                                        ft.Text(
                                            "©2024 SDSystems Inc. | All rights reserved.",
                                            size = 12,
                                            color = mainfont,
                                            text_align = 'center'
                                        )
                                    ]
                                )
                            ]
                        )
                    )
                ]
            )
        )
        
        if page.route == "/dash":
            page.views.append(
                ft.View(
                    "/dash",
                    [
                        ft.CupertinoAppBar(
                            leading = ft.IconButton(
                                icon = ft.icons.MENU_ROUNDED,
                                scale = 0.85,
                                icon_color = mainfont,
                                on_click = show_drawer
                            ),
                            middle = top_img,
                            trailing = ft.IconButton(
                                scale = 0.85,
                                icon = ft.icons.DARK_MODE_ROUNDED,
                                icon_color = mainfont,
                                on_click = lambda e: toggle_theme(e)
                            )
                        ),
                        ft.SafeArea(
                            minimum = 5,
                            content = ft.Column(
                                alignment = 'center',
                                spacing = 0,
                                controls = [
                                    ft.Row(
                                        alignment = 'center',
                                        controls = [
                                            ft.Text(
                                                "Body",
                                                size = 10,
                                                color = mainfont
                                            )
                                        ]
                                    )
                                ]
                            )
                        )
                    ]
                )
            )
            
        page.update()
        
    def show_drawer(e):
        page.drawer = drawer
        drawer.open = True
        drawer.update()
        
    def toggle_theme(e):
        if e.control.icon == ft.icons.LIGHT_MODE_ROUNDED:
            page.theme_mode = ft.ThemeMode.DARK
            e.control.icon = ft.icons.DARK_MODE_ROUNDED
        
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
            e.control.icon = ft.icons.LIGHT_MODE_ROUNDED
            
        page.update()
    
    #pops-up when the user entered a blank password
    def open_dlg_modal_noinp (e):
        page.dialog = dlg_modal_noinp
        dlg_modal_noinp.open = True
        page.update()
        
    def open_dlg_modal (e):
        page.dialog = dlg_modal
        dlg_modal.open = True
        page.update()
        
    def close_dlg(e):
        dlg_modal.open = False
        dlg_modal_noinp.open = False
        page.update()
        
    def login(e):
        v = passw.value
        query = "SELECT * FROM login WHERE password = %s"
        data = (v,)
        cursor.execute(query, data)
        result = cursor.fetchall()
        
        if len(v) == 0:
            print('failed.')
            open_dlg_modal_noinp(e)
        elif(result):
            print('login success.')
            page.go("/dash")
        else:
            print('login failed.')
            open_dlg_modal(e)

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main, view=ft.AppView.WEB_BROWSER)