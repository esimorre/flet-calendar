from datetime import datetime

import flet as ft
from controls import Month


class CalendarApp(ft.Column):
    nb_monthes = 3
    def __init__(self):
        super().__init__()
        now = datetime.now()

        self.width = 400
        self.controls = []
        for m in range(self.nb_monthes):
            self.controls.append( Month(2024, now.month + m) )

class Drawer(ft.NavigationDrawer):

    def __init__(self):
        super().__init__(
        controls=[
            ft.Container(height=12),
            ft.NavigationDrawerDestination(
                label="Item 1",
                icon=ft.icons.DOOR_BACK_DOOR_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.DOOR_BACK_DOOR),
            ),
            ft.Divider(thickness=2),
            ft.NavigationDrawerDestination(
                icon_content=ft.Icon(ft.icons.MAIL_OUTLINED),
                label="Item 2",
                selected_icon=ft.icons.MAIL,
            ),
            ft.NavigationDrawerDestination(
                icon_content=ft.Icon(ft.icons.PHONE_OUTLINED),
                label="Item 3",
                selected_icon=ft.icons.PHONE,
            ),
        ],
        )

def main(page: ft.Page):

    drawer = Drawer()
    def on_pan(e: ft.DragUpdateEvent):
        print(e)
    def on_sidebar(e : ft.ControlEvent):
        print("on_sidebar", e)
        page.open(drawer)

    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.icons.EXPLORE, label="Explore"),
            ft.NavigationBarDestination(icon=ft.icons.COMMUTE, label="Commute"),
            ft.NavigationBarDestination(
                icon=ft.icons.BOOKMARK_BORDER,
                selected_icon=ft.icons.BOOKMARK,
                label="Explore",
            ),
        ],
        on_change=on_sidebar
    )
    print("print Hello", page.url)
    page.title = "Calendar"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.ADAPTIVE

    gd = ft.GestureDetector(
        on_horizontal_drag_update=on_pan,
        drag_interval=500,
        content=CalendarApp()
    )

    page.add(gd)

ft.app(target=main, assets_dir="assets", view=ft.AppView.WEB_BROWSER)