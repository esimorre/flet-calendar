import flet as ft
from controls import Month, MonthHeader


class CalendarApp(ft.Column):
    def __init__(self):
        super().__init__()

        self.width = 600
        self.controls = [
            Month(2024, 10)
        ]


def main(page: ft.Page):

    page.title = "Calendar"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.ADAPTIVE

    page.add(CalendarApp())

ft.app(main)