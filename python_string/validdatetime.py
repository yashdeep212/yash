
import datetime 
def validdate(day, month, year):
      	isValid = True   
	try :
		datetime.datetime(int(year),int(month), int(day)) 
	except ValueError:
		isValid = False
	if(isValid):
		print ("given date is valid")
	else:
		print ("given date is not valid")
  
validdate(10,12,2000)
validdate(31,11,2000)

