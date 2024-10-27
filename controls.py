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
    def __init__(self, year : int, month : int, mdays : list[(int, int)], num_week=None,
                 bgcolor=ft.colors.TRANSPARENT):
        super().__init__(spacing=2)
        self.year = year
        self.month = month
        self.week = num_week
        if num_week:
            obweek = ft.Container(
                    content=ft.Text(value=num_week),
                    alignment=ft.alignment.center,
                    margin=0,
                    width=30,
                    height=30,
                    bgcolor=bgcolor,
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

    def traverse_weeks(self, func : callable):
        if self.week:
            func(self.controls[0], self.year, self.month, self.week)

    def traverse_days(self, func: callable):
        start = 1 if self.week else 0
        for c in self.controls[start:]:
            func(c, self.year, self.month, c.controls[0].value)



class Month(ft.Column):
    def __init__(self, year : int, month : int):
        super().__init__(spacing=4)
        self.year = year
        self.month = month
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
            bg = ft.colors.TRANSPARENT
            if numw%2 == 0: bg = ft.colors.GREEN
            self.controls.append(Week(year, month, wdays, numw, bgcolor=bg))

    def traverse_weeks(self, func : callable):
        for c in self.controls[2:]:
            c.traverse_weeks()

    def traverse_days(self, func: callable):
        for c in self.controls[2:]:
            c.traverse_days()

