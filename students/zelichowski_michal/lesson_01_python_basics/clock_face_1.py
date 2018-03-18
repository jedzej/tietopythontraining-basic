# H hours, M minutes and S seconds are passed since the midnight (0 ≤ H < 12, 0 ≤ M < 60, 0 ≤ S < 60).
# Determine the angle (in degrees) of the hour hand on the clock face right now

DEG_PER_HOUR = 30
DEG_PER_MINUTE = hour / 60
DEG_PER_SECOND = hour / 3600

h = int(input())
m = int(input())
s = int(input())

print(h*DEG_PER_HOUR + m*DEG_PER_MINUTE + s*DEG_PER_SECOND)
