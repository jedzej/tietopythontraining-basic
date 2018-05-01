# H hours, M minutes and S seconds are passed since the midnight (0 ≤ H < 12, 0 ≤ M < 60, 0 ≤ S < 60).
# Determine the angle (in degrees) of the hour hand on the clock face right now.

# Read an integer:
H = int(input())
M = int(input())
S = int(input())
sec_in_h = 3600
sec_in_m = 60
sec_in_half_day = 43200     #12 * 3600
# Print a value:
# print(a)
total_sec = H*sec_in_h + M*sec_in_m + S
angle = total_sec / sec_in_half_day
print(angle*360)