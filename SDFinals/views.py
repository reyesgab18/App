from flet import *

def views_handler(page):
    return {
        '/':View(
                route = '/',
                controls = [
                    Container(
                        height = 800,
                        width = 350,
                        bgcolor = 'red',
                    )
                ]
            ),
        '/login':View(
                route = '/login',
                controls = [
                    Container(
                        height = 800,
                        width = 350,
                        bgcolor = 'blue',
                    )
                ]
            )
    }