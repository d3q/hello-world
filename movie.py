#The purpose of this lesson is to teach you how to structure classes that need other classes inside other files.

import os
import time

def listdir_nohidden(path):
    for f in os.listdir(path):
        if not f.startswith('.'):
            yield f


default_sleep_time = 1410
target_sleep_time = default_sleep_time
current_time = time.localtime()
print(f"现在是{time.strftime('%H点%M分(%-m月%e日, %a)',current_time)}")

current_time_hour = int(time.strftime('%H',current_time))
current_time_min = int(time.strftime('%M',current_time))

#time_until_sleep is an int
time_until_sleep = target_sleep_time - (current_time_hour * 60 + current_time_min)

print(f"距离11点30分睡觉还有 {int((time_until_sleep - (time_until_sleep % 60)) / 60)}小时{time_until_sleep % 60}分 可以用来看电影")


#filename = os.path.basename('/Users/xuguangzhu/Coding/hello-world/ex115.py')

movie_list = listdir_nohidden('/Volumes/Seagate_4T/movies/单独电影')

print("asd",*sorted(movie_list), sep = "\n")
#print(type(filename))