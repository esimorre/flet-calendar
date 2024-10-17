import flet as ft
from mycalendar import MyCalendar

calendar = MyCalendar(firstweekday=0, locale="fr")

class MonthHeader(ft.Row):
    def __init__(self):
        super().__init__(spacing=2)
        for day in calendar.days_week_labels():
            obday = ft.Container(
                    content=ft.Text(value=day),
                    alignment=ft.alignment.center,
                    margin=0,
                    width=30,
                    height=30,
                    bgcolor=ft.colors.AMBER,
                    border_radius=ft.border_radius.all(5))
            self.controls.append(obday)

class Week(ft.Row):
    def __init__(self, year : int, month : int, mdays : list[(int, int)]):
        super().__init__(spacing=2)
        for month2, day in mdays:
            obday = ft.Container(
                    content=ft.Text(value=day),
                    alignment=ft.alignment.center,
                    margin=0,
                    width=30,
                    height=30,
                    bgcolor=ft.colors.BLUE_50,
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

        mdays = []
        for i, q in enumerate(calendar.itermonthdays4(year, month)):
            w, m, d, wd = q
            mdays.append((m, d))
            if wd == 6:
                self.controls.append(Week(year, month, mdays))
                mdays.clear()

