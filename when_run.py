from time import sleep
from time import time, ctime
import keyboard


def whenrun(day,hour,minute):
    time_3 = ['', '', '']
    while str(hour) != time_3[0] or str(minute) != time_3[1] or str(day) != w_day:
        time_now = ctime(time())
        time_now_clock = time_now.split(' ')
        w_day = time_now_clock[3]
        time_2 = time_now_clock[4]
        time_3 = time_2.split(':')
        sleep(1)

day = input("when day of month to do : ")
hour = input("when hour to do : ")
minute = input("when minute to do : ")

whenrun(day,hour,minute)

#program code ...
