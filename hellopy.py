import time
import math

localtime = time.localtime(time.time())
print ("Local current time :", localtime)

ticks = time.time()
print ("Number of ticks since 12:00am, January 1, 1970:", ticks)


now = time.time()
print ("now", now)


import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%H:%M"))



seconds_since_midnight = (now - now.replace(hour=23, minute=30, second=0, microsecond=0)).total_seconds()


hour_to_24=24-seconds_since_midnight/3600

print ("123", hour_to_24)

hour_to_24_2=hour_to_24 // 1

print ("hour_to_24  is ", int(hour_to_24_2)-24)

min_to_24=(hour_to_24%1) *60
min_to_24 = min_to_24 // 1

print ("min_to_24 is ", int(min_to_24))

