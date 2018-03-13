'''
title: digital_clock
author: arkadiusz.kasprzyk@tieto.com
date: 2018-03-05
description:
    Given the integer N - the number of minutes that is passed since midnight
    - how many hours and minutes are displayed on the 24h digital clock?

    The program should print two numbers: the number of hours (between 0 and 23)
    and the number of minutes (between 0 and 59).

    For example, if N = 150, then 150 minutes have passed since midnight - i.e. now is 2:30 am.
    So the program should print 2 30.
'''

import math as m
print("The hour (on 24-hour clock) based on the number of minutes passed since midnight.")

m = int(input("Give a number of minutes: "))

hh = m // 60
mm = m % 60

print("It's {}:{}.".format(hh,mm))


input("Press Enter to quit the program.")