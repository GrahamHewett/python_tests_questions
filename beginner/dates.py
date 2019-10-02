from datetime import date
import time
import datetime
import calendar

def main():
	print ("Today's date is ", date.today())
main()

def get_week_day(day, month, year):
	date1 = datetime.datetime(year, month, day)
	days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
	print ('The', date1.date(), 'was a '+ days[date1.weekday()])

(get_week_day(13, 5, 1986))

2 days/months/years before a given date was 

def format_dates():
	#strtime
	#
	return;

def format_times():
	#strtime
	#
	return;

def is_leap_year(year):
	return calendar.isleap(year)
print(is_leap_year(2019))