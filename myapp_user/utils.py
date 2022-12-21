from datetime import datetime, timedelta
from calendar import HTMLCalendar
from .models import Event

class Calendar(HTMLCalendar):
	def __init__(self, year=None, month=None):
		self.year = year
		self.month = month
		super(Calendar, self).__init__()

# จัดรูปแบบวันเป็น td
# filter กิจกรรมตามวัน
	def formatday(self, day, events):
		events_per_day = events.filter(start_time__day=day)
		d = ''
		for event in events_per_day:
			d += f'<li> {event.name} </li>'

		if day != 0:
			return f"<td class='text-start'><span class='date'><br>{day}</span><ul> {d} </ul></td>"
		return '<td></td>'

# จัดรูปแบบ weeks เป็น tr 
	def formatweek(self, theweek, events):
		week = ''
		for d, weekday in theweek:
			week += self.formatday(d, events)
		return f'<tr> {week} </tr>'

# จัดรูปแบบเดือนเป็นตาราง
# filter กิจกรรมตามปีและเดือน
	def formatmonth(self, withyear=True):
		events = Event.objects.filter(start_time__year=self.year, start_time__month=self.month)

		cal = f'<table border="5" cellpadding="5" cellspacing="5" class="table table-striped table-warning calendar">\n'
		cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
		cal += f'{self.formatweekheader()}\n'
		for week in self.monthdays2calendar(self.year, self.month):
			cal += f'{self.formatweek(week, events)}\n'
		return cal