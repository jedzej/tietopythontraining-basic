#!/usr/bin/env python3

try:
    hour_angle_since_midnight = float(input("Please enter a number:\n"))
except ValueError:
    print('That was not a valid number, please try again')
    exit()

full_hour_circle_in_seconds = 12 * 3600
seconds_passed = hour_angle_since_midnight / 360 * full_hour_circle_in_seconds
seconds_passed_from_current_hour = seconds_passed % 3600
full_minute_circle_in_seconds = 60 * 60
minutes_angle = 360 * seconds_passed_from_current_hour \
                / full_minute_circle_in_seconds

print(minutes_angle)
