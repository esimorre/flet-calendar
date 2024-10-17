import unittest
from datetime import datetime

from mycalendar import MyCalendar


class TestCalendar(unittest.TestCase):

    def test_basic(self):
        cal = MyCalendar(firstweekday=0, locale="fr")
        now = datetime.now()
        for q in cal.itermonthdays4(now.year, now.month):
            w, m, d, wd = q
            print(q)
        print(cal.days_week_labels())
        print(cal.formatmonthname(now.year, now.month, 30, withyear=False))

