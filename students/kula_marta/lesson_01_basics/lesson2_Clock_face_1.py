#!/usr/bin/env python

T_ONE_SEC = 12 * 60 * 60

h = int(input("h: "))
m = int(input("m: "))
s = int(input("s: "))

sec_total = (h * 3600) + (m * 60) + s
w = float(sec_total * 360) / T_ONE_SEC
w = round(w, 3)  # zaokraglanie do 3 miejsc po ,
print("current angle in the hour hand steps on the clock face w = %0.3f" % w)
