from datetime import datetime
 

date_format = "%m-%d-%Y %H:%M:%S"
 
try:
	time1  = datetime.strptime('2008-01-2008 00:00:00', date_format)
	time2  = datetime.strptime('8-02-2008 01:30:00', date_format)
except:ValueError
	print("Incorrect date format, should be DD-MM-YYYY")
 

diff = time2 - time1
print(diff)
 
 

print ('Days & Overall hours from the above two dates')

days = diff.days
print (str(days) + ' day(s)')
 

days_to_hours = days * 24
diff_btw_two_times = (diff.seconds) / 3600
overall_hours = days_to_hours + diff_btw_two_times
print (str(overall_hours) + ' hours');
  
print ('\nTime difference between two times (date is not considered)')
 
hours = (diff.seconds) / 3600  
print (str(hours) + ' Hours')
  
minutes = (diff.seconds) / 60
print (str(minutes) + ' Minutes')
  
print (str(diff.seconds) + ' secs')