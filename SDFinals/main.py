"""
Flet Mobile Application
"""

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
db = mysql.connector.connect(host = db_host, user = db_user, password = db_password, database = db_name, port = int(db_port))
cursor = db.cursor()

#base view
class BaseView(ft.View):
    def __init__(
        self,
        page: ft.Page,
        route: str,
        route_to: str
    ):
        self.page = page
        self.route_to = route_to
        
        self.image = ft.Image(
            src = f"https://lh3.googleusercontent.com/a/ACg8ocIAY8jNypsDprgge-kJJF_wjgGu8MZw4mKBIo9IOlfu1Igmq5T4UeEA-YWAD94p-QS014v7Ay2Gk1EMzzU71iiyeg=s360-c-no",
            height = 300,
            width = 300
        )
        
        self.passw = ft.TextField(
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
            on_submit = self.login
        )
        
        self.dlg_modal = ft.AlertDialog(
            modal=True,
            content=ft.Text(
                "Wrong password. Please try again.",
                color = mainfont
                ),
            actions=[
                ft.TextButton(
                    "Ok",
                    on_click = self.close_dlg,
                    style = ft.ButtonStyle(
                        color = backfont,
                        bgcolor = mainfont
                    )
                )
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        
        self.dlg_modal_noinp = ft.AlertDialog(
            modal=True,
            content=ft.Text(
                "Please input field.",
                color = mainfont
                ),
            actions=[
                ft.TextButton(
                    "Ok",
                    on_click = self.close_dlg,
                    style = ft.ButtonStyle(
                        color = backfont,
                        bgcolor = mainfont
                    )
                )
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        
        self.filledbutton = ft.FilledButton(
            text = "Log In",
            style = ft.ButtonStyle(
                bgcolor = mainfont,
                
            ),
            on_click = self.login
        )
        
        super().__init__()
        
        if page.route == "/":
            self.controls = [
                ft.SafeArea(
                minimum = 5,
                content = ft.Column(
                    alignment = "center",
                    spacing = 0,
                    controls = [
                        ft.Row(
                            alignment = "end",
                            controls = [
                                ft.IconButton(
                                    scale = 0.85,
                                    icon = ft.icons.DARK_MODE_ROUNDED,
                                    icon_color = mainfont,
                                    on_click = lambda e: self.toggle_theme(e)
                                )
                            ]
                        ),
                        ft.Divider(height = 10, color = "transparent"),
                        ft.Row(
                            alignment = "center",
                            controls = [
                                self.image
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
                                self.passw
                            ]
                        ),
                        ft.Divider(height = 10, color = "transparent"),
                        ft.Row(
                            alignment = "center",
                            controls = [
                                self.filledbutton
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
                                    f"Password: {self.password}"
                                )
                            ]
                        )
                    ]
                )
            )
        ]
    
        if page.route == "/dash":
            self.controls = [
                ft.SafeArea(
                    minimum = 5,
                    content = ft.Column(
                        alignment = "center",
                        spacing = 0,
                        controls = [
                            ft.Row(
                                alignment = "center",
                                controls = [
                                    ft.Text(
                                        "fuck",
                                        size = 10
                                    )
                                ]
                            )
                        ]
                    )
                )
            ]
            
    def routing(self):
        time.sleep(1.9)
        self.page.go(self.route_to)
        
    def go_dash(self, e):
        self.page.route = "/dash"
        self.page.update()
    
    def getpass (self, e):
        query = "SELECT password FROM login"
        cursor.execute(query)
        result = cursor.fetchone()
        password = result[0]
        print("password used: " + password)
        
    def login(self, e):
        v = self.passw.value
        query = "SELECT * FROM login WHERE password = %s"
        data = (v,)
        cursor.execute(query, data)
        result = cursor.fetchall()
        
        if len(v) == 0:
            print('failed.')
            self.open_dlg_modal_noinp(e)
        elif(result):
            print('login success.')
            self.getpass(e)
            self.routing()
        else:
            print('login failed.')
            self.open_dlg_modal(e)
            
    def open_dlg_modal_noinp (self, e):
        self.page.dialog = self.dlg_modal_noinp
        self.dlg_modal_noinp.open = True
        self.page.update()
            
    def open_dlg_modal(self, e):
        self.page.dialog = self.dlg_modal
        self.dlg_modal.open = True
        self.page.update()
        
    def close_dlg(self, e):
        self.dlg_modal.open = False
        self.dlg_modal_noinp.open = False
        self.page.update()
        
    def toggle_theme(self, e):
        if e.control.icon == ft.icons.LIGHT_MODE_ROUNDED:
            self.page.theme_mode = ft.ThemeMode.DARK
            e.control.icon = ft.icons.DARK_MODE_ROUNDED
        
        else:
            self.page.theme_mode = ft.ThemeMode.LIGHT
            e.control.icon = ft.icons.LIGHT_MODE_ROUNDED
            
        self.page.update()

#login view     
class LoginView(BaseView): #inherits BaseView class
    def __init__(
        self,
        page: ft.Page,
        route = "/",
        route_to = "/dash"
    ):
        super().__init__(
            page = page,
            route = route,
            route_to = route_to
        )

class DashView(BaseView): #inherits BaseView class
    def __init__(
        self,
        page: ft.Page,
        route = "/dash",
        route_to = "/"
    ):
        super().__init__(
            page = page,
            route = route,
            route_to = route_to
        )

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK
    
    theme = ft.Theme()
    theme.page_transitions.ios = ft.PageTransitionTheme.NONE
    theme.page_transitions.macos = ft.PageTransitionTheme.NONE
    page.theme = theme
    
    login = LoginView(page)
    dash = DashView(page)
    
    print("current page: " + page.route)
    
    def change_route():
        page.views.clear()
        
        if page.route == "/":
            page.views.append(login)
            print(page.route)
        
        if page.route == "/dash":
            page.views.append(dash)
            print(page.route)
            
        page.update()
        
    ##page.on_route_change = change_route
    page.views.append(login)
    
    page.update()
    
ft.app(
    target = main,
    assets_dir = "assets"
)
    
    