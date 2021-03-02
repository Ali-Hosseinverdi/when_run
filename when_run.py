import keyboard
from time import sleep
from time import time, ctime

def whenrun(hour,minute):
    time_3 = ['', '', '']
    while str(hour) != time_3[0] or str(minute) != time_3[1]:
        time_now = ctime(time())
        time_now_clock = time_now.split(' ')
        time_2 = time_now_clock[3]
        time_3 = time_2.split(':')
        sleep(1)

hour = input("when hour to do : ")
minute = input("when minute to do : ")

whenrun(hour,minute)
