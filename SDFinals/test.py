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

def main(page: ft.Page):
    page.title = "Routes Example"

    page.theme_mode = ft.ThemeMode.DARK
    
    theme = ft.Theme()
    theme.page_transitions.ios = ft.PageTransitionTheme.NONE
    theme.page_transitions.macos = ft.PageTransitionTheme.NONE
    page.theme = theme
    
    image = ft.Image(
        src = f"https://lh3.googleusercontent.com/a/ACg8ocIAY8jNypsDprgge-kJJF_wjgGu8MZw4mKBIo9IOlfu1Igmq5T4UeEA-YWAD94p-QS014v7Ay2Gk1EMzzU71iiyeg=s360-c-no",
        height = 300,
        width = 300
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
        on_submit = lambda e: login (e)
    )
    
    dlg_modal = ft.AlertDialog(
        modal=True,
        content=ft.Text(
            "Wrong password. Please try again.",
            color = mainfont
            ),
        actions=[
            ft.TextButton(
                "Ok",
                on_click = lambda e: close_dlg (e),
                style = ft.ButtonStyle(
                    color = backfont,
                    bgcolor = mainfont
                )
            )
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )
    
    dlg_modal_noinp = ft.AlertDialog(
        modal=True,
        content=ft.Text(
            "Please input field.",
            color = mainfont
            ),
        actions=[
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
    
    filledbutton = ft.FilledButton(
        text = "Log In",
        style = ft.ButtonStyle(
            bgcolor = mainfont,
            
        ),
        on_click = lambda e: login(e)
    )

    def route_change(route):
        password1 = getpass()
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
                                    alignment = "end",
                                    controls = [
                                        ft.IconButton(
                                            scale = 0.85,
                                            icon = ft.icons.DARK_MODE_ROUNDED,
                                            icon_color = mainfont,
                                            on_click = lambda e: toggle_theme(e)
                                        )
                                    ]
                                ),
                                ft.Divider(height = 10, color = "transparent"),
                                ft.Row(
                                    alignment = "center",
                                    controls = [
                                        image
                                    ]
                                ),
                                ft.Row(
                                    alignment = "center",
                                    controls = [
                                        ft.Divider(
                                            height = 20
                                        )
                                    ]
                                ),
                                ft.Row(
                                    alignment = "center",
                                    controls = [
                                        passw
                                    ]
                                ),
                                ft.Divider(height = 10, color = "transparent"),
                                ft.Row(
                                    alignment = "center",
                                    controls = [
                                        filledbutton
                                    ]
                                ),
                                ft.Divider(height = 180, color = "transparent"),
                                ft.Row(
                                    alignment = "center",
                                    controls = [
                                        ft.Text(
                                            "Forgot password? Contact sd.group5@gmail.com",
                                            size = 12,
                                            weight = ft.FontWeight.BOLD,
                                            color = mainfont,
                                            text_align = "center"
                                        )
                                    ]
                                ),
                                ft.Row(
                                    alignment = "center",
                                    controls = [
                                        ft.Text(
                                            "©2024 SDSystems Inc. | All rights reserved.",
                                            size = 12,
                                            color = mainfont,
                                            text_align = "center"
                                        )
                                    ]
                                ),
                                ft.Row(
                                    alignment = "center",
                                    controls = [
                                        ft.Text(
                                            f"Password: {password1}"
                                        )
                                    ]
                                )
                            ]
                        )
                    ),
                    
                    """ft.AppBar(title=ft.Text("Flet app"), bgcolor=ft.colors.SURFACE_VARIANT),
                    ft.ElevatedButton("Visit Store", on_click=lambda _: page.go("/store")),"""
                ],
            )
        )
        if page.route == "/store":
            page.views.append(
                ft.View(
                    "/store",
                    [
                        ft.AppBar(title=ft.Text("Store"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                    ],
                )
            )
        
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)
        
    def toggle_theme(e):
        if e.control.icon == ft.icons.LIGHT_MODE_ROUNDED:
            page.theme_mode = ft.ThemeMode.DARK
            e.control.icon = ft.icons.DARK_MODE_ROUNDED
        
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
            e.control.icon = ft.icons.LIGHT_MODE_ROUNDED
            
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
            getpass(e)
            page.go("/store")
        else:
            print('login failed.')
            open_dlg_modal(e)
            
    def getpass ():
        query = "SELECT password FROM login"
        cursor.execute(query)
        result = cursor.fetchone()
        password = result[0]
        print("password used: " + password)
        return (password)

    def open_dlg_modal_noinp (e):
        page.dialog = dlg_modal_noinp
        dlg_modal_noinp.open = True
        page.update()
            
    def open_dlg_modal(e):
        page.dialog = dlg_modal
        dlg_modal.open = True
        page.update()
        
    def close_dlg(e):
        dlg_modal.open = False
        dlg_modal_noinp.open = False
        page.update()

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main)
