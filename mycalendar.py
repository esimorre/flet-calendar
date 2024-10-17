from calendar import LocaleTextCalendar


class MyCalendar(LocaleTextCalendar):

    def days_week_labels(self, len : int = 2):
        return [self.formatweekday(i, 2) for i in self.iterweekdays()]

    def month_name(self, year : int, month : int):
        return self.formatmonthname(year, month, 30, withyear=False)
