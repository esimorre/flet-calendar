import flet as ft
from mycalendar import MyCalendar

calendar = MyCalendar(firstweekday=0, locale="fr")

class MonthHeader(ft.Row):
    def __init__(self, num_week=True):
        super().__init__(spacing=2)
        if num_week:
            obweek = ft.Container(
                    content=ft.Text(value="S"),
                    alignment=ft.alignment.center,
                    margin=0,
                    width=30,
                    height=30,
                    bgcolor=ft.colors.TRANSPARENT,
                    border_radius=ft.border_radius.all(5))
            self.controls.append(obweek)

        for day in calendar.days_week_labels():
            obday = ft.Container(
                    content=ft.Text(value=day),
                    alignment=ft.alignment.center,
                    margin=0,
                    width=30,
                    height=30,
                    bgcolor=ft.colors.TRANSPARENT,
                    border_radius=ft.border_radius.all(5))
            self.controls.append(obday)

class Week(ft.Row):
    def __init__(self, year : int, month : int, mdays : list[(int, int)], num_week=None):
        super().__init__(spacing=2)
        if num_week:
            obweek = ft.Container(
                    content=ft.Text(value=num_week),
                    alignment=ft.alignment.center,
                    margin=0,
                    width=30,
                    height=30,
                    bgcolor=ft.colors.TRANSPARENT,
                    border_radius=ft.border_radius.all(5))
            self.controls.append(obweek)
            mdays = [reversed(p) for p in mdays]

        for _, day in mdays:
            color = ft.colors.TRANSPARENT
            content = None
            if day > 0:
                content = ft.Text(value=day)
                color = ft.colors.AMBER
            obday = ft.Container(
                    content=content,
                    alignment=ft.alignment.center,
                    margin=0,
                    width=30,
                    height=30,
                    bgcolor=color,
                    border_radius=ft.border_radius.all(5))
            self.controls.append(obday)

class Month(ft.Column):
    def __init__(self, year : int, month : int):
        super().__init__(spacing=4)
        self.controls = [
            ft.Row(
            [ft.Text(value=calendar.month_name(year, month),
                    theme_style=ft.TextThemeStyle.HEADLINE_MEDIUM)],
                    alignment=ft.MainAxisAlignment.START,
            ),
            MonthHeader()
        ]

        for wdata in calendar.monthdays2calendar_ext(year, month):
            numw, wdays = wdata
            self.controls.append(Week(year, month, wdays, numw))

