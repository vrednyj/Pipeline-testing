"""
utils.py contains classes to work with calendar.
"""

from typing import Callable
from .views import Attraction
from datetime import datetime, timedelta
from calendar import HTMLCalendar
from .models import Booking, Location


class Calendar(HTMLCalendar):
    """
    A class to represent a calendar.

    Attributes
    ----------
    attractions : Any
        name of the attractions
    year : Any
        year of the calendar
    month : Any
        month of the calendar

    Methods
    -------
    formatday (additional=""):
        Prints the person's name and age.

    """
    def __init__(self, year, month, attractions):
        """
        Constructor
        """
        super(Calendar, self).__init__()
        self.attractions = attractions
        self.year = year
        self.month = month

    # formats a day as a td
    # filter events by day
    def formatday(self, day, events):
        """
        :return: "<td><span class='date'>{day}</span><ul> {d} </ul></td>"
        :rtype: str
        """
        events_per_day = []
        for attraction in self.attractions:
            events_per_day += events.filter(start_time__day=day, title=attraction.title)
        d = ''
        for event in events_per_day:
            d += f'{event.get_html_title}</br>'

        if day != 0:
            return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
        return '<td></td>'

    # formats a week as a tr
    def formatweek(self, theweek, events):
        """
        Formats the week
        :return: '<tr> {week} </tr>'
        :rtype: str
        """
        week = ''
        for d, weekday in theweek:
            week += self.formatday(d, events)
        return f'<tr> {week} </tr>'

    # formats a month as a table
    # filter events by year and month

    # noinspection PyMissingOrEmptyDocstring
    def formatmonth(self, withyear=True):
        """
        Formats a month as a table
        Filter events by year and month
        """
        events = Booking.objects.filter(start_time__year=self.year, start_time__month=self.month)
        cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
        cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week, events)}\n'
        return cal
