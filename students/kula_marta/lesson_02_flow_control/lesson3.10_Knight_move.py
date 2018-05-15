#!/usr/bin/env python

#from math import fabs

MV_LONG = 2
MV_SHORT = 1

BOARD_MIN_FIELD = 0
BOARD_MAX_FIELD = 8

start_x = int(input("give 1-x: "))
start_y = int(input("give 1-y: "))

stop_x = int(input("give 2-x: "))
stop_y = int(input("give 2-y: "))

tab = [2*[10]]*4

is_ok = 0

#check on x
if (stop_x == start_x + 2 and stop_x <= BOARD_MAX_FIELD) or (stop_x == start_x - 2 and stop_x >= BOARD_MIN_FIELD):
    if (stop_y == start_y + 1 and stop_y <= BOARD_MAX_FIELD) or (stop_y == start_y - 1 and stop_y >= BOARD_MIN_FIELD):
        is_ok = 1

#check on y
if (stop_y == start_y + 2 and stop_y <= BOARD_MAX_FIELD) or (stop_y == start_y - 2 and stop_y >= BOARD_MIN_FIELD):
    if (stop_x == start_x + 1 and stop_x <= BOARD_MAX_FIELD) or (stop_x == start_x - 1 and stop_x >= BOARD_MIN_FIELD):
        is_ok = 1

#print result
if is_ok == 1:
    print ("YES")
else:
    print ("NO")
