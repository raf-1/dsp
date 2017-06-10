# Hint:  use Google to find python function
import time
import calendar
from datetime import date
####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   

date_start_list = date_start.split("-")
date_start_list = [ int(x) for x in date_start_list]
date_stop_list = date_stop.split("-")
date_stop_list = [ int(x) for x in date_stop_list]
days_between = date(date_stop_list[2], date_stop_list[0], date_stop_list[1]) - date(date_start_list[2], date_start_list[0], date_start_list[1])

print (days_between.days, "days")
####b)  
date_start = '12312013'  
date_stop = '05282015'  

days_between = date(int(date_stop[4:]), int(date_stop[0:2]), int(date_stop[2:4])) - date(int(date_start[4:]), int(date_start[0:2]), int(date_start[2:4]))

print (days_between.days, "days")

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  

date_start_list = date_start.split("-")
date_stop_list = date_stop.split("-")

days_between = date(int(date_stop_list[2]), list(calendar.month_abbr).index(date_stop_list[1]), int(date_stop_list[0])) - date(int(date_start_list[2]), list(calendar.month_abbr).index(date_stop_list[1]), int(date_start_list[0]))


print (days_between.days, "days")
