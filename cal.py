import calendar

c = calendar.HTMLCalendar(firstweekday=0)
print(c.formatmonth(2018, 3, withyear=True))