from calendar import LocaleTextCalendar


class MyCalendar(LocaleTextCalendar):
    # year -> [num_week1, ...]
    _nbweek_monthes = {}
    def __init__(self, firstweekday, locale):
        super().__init__(firstweekday, locale)

    def _update_data(self, year : int):
        if year not in self._nbweek_monthes:
            num = 1
            weeks_data = self.monthdays2calendar(year,1)
            if weeks_data[0][0][1] in (1, 2, 3): num = 2
            data = [num]
            for m in range(1, 12):
                weeks_data = self.monthdays2calendar(year, m + 1)
                nbweeks = len(weeks_data)
                num = num + nbweeks
                if weeks_data[0][0][1] < m : num -= 1
                data.append( num)
            self._nbweek_monthes[year] = data

    def monthdays2calendar_ext(self, year : int,  month : int):
        """ extends monthdays2calendar with num weeks """
        self._update_data(year)
        w1 = self._nbweek_monthes[year][month-1]
        md2c = self.monthdays2calendar(year, month)
        return [(w1+ns, ls) for ns, ls in enumerate(md2c)]

    def days_week_labels(self, len : int = 2):
        return [self.formatweekday(i, len) for i in self.iterweekdays()]

    def month_name(self, year : int, month : int):
        return self.formatmonthname(year, month, 30, withyear=False)
