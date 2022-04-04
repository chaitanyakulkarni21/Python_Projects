# Count down Timer using Python

import time 

def countDown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end= "\r")
        time.sleep(1)
        t = t - 1

    print('Time up!!!')


t = int(input('Enter time in seconds: '))
countDown(t)