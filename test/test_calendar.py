import unittest
from datetime import datetime

from mycalendar import MyCalendar


class TestCalendar(unittest.TestCase):

    def setUp(self):
        self.cal = MyCalendar(firstweekday=0, locale="fr")

    def test_basic(self):
        cal = self.cal
        now = datetime.now()
        for q in cal.itermonthdays4(now.year, now.month):
            w, m, d, wd = q
            print(q)
        print(cal.days_week_labels())
        print(cal.formatmonthname(now.year, now.month, 30, withyear=False))

    def test_monthdays2calendar(self):
        print(self.cal.monthdays2calendar(2024, 1))
        print(self.cal.monthdays2calendar(2024, 2))

    def test_monthdays2calendar_ext(self):
        print(self.cal.monthdays2calendar_ext(2024, 1))
        print(self.cal.monthdays2calendar_ext(2024, 12))
        print(self.cal.monthdays2calendar_ext(2025, 1))