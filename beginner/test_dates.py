from datetime import date
import time
import datetime

def main():
	print ("Today's date is ", date.today())
main()

def get_week_day(day, month, year):
	date1 = datetime.datetime(year, month, day)
	days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
	print ('The', date1.date(), 'was a '+ days[date1.weekday()])

(get_week_day(13, 5, 1986))

def formatDates():
	#strtime
	#
	return;

def formatTimes():
	#strtime
	#
	return;
