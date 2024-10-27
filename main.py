from datetime import datetime, timedelta

import flet as ft
from controls import Month


class CalendarApp(ft.Column):
    nb_monthes = 3
    def __init__(self, dtime : datetime):
        super().__init__()

        self.width = 400
        self.controls = []
        for m in range(self.nb_monthes):
            self.controls.append( Month(2024, dtime.month + m) )

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

class CalendarCache:
    def __init__(self):
        self.cache = {}

    def get(self, dtime : datetime):
        key = "%d:%d" % (dtime.year, dtime.month)
        if key not in self.cache:
            self.cache[key] = CalendarApp(dtime)
        return self.cache[key]

class PanGesture(ft.GestureDetector):
    def __init__(self, now : datetime):
        super().__init__(
        on_horizontal_drag_update=self.on_pan,
        drag_interval=500,
        )
        self.current = now
        self.cache = CalendarCache()
        self.content = self.cache.get(now)

    def on_pan(self, e: ft.DragUpdateEvent):
        dmonth = timedelta(weeks=CalendarApp.nb_monthes*4)
        if e.primary_delta < 0: dmonth *= -1
        self.current += dmonth
        print(e.primary_delta, self.current)
        self.content = self.cache.get(self.current)
        self.page.update()

def main(page: ft.Page):
    now = datetime.now()
    drawer = Drawer()


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

    gd = PanGesture(now)

    page.add(gd)

ft.app(target=main, assets_dir="assets", view=ft.AppView.WEB_BROWSER)