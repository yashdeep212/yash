

import calendar 
  
def findtheDay(date): 
    day, month, year = (int(i) for i in date.split(' '))  
    print(day, month, year)   
    dayNumber = calendar.weekday(year, month, day) 
    print(dayNumber)
    days =["Monday", "Tuesday", "Wednesday", "Thursday", 
                         "Friday", "Saturday", "Sunday"] 
    return (days[dayNumber]) 
  
# Driver program 
date = '03 02 2019'
print(findtheDay(date)) 