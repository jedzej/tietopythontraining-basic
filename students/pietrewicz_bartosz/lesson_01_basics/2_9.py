# Read the number of hours (H), minutes (M) and seconds (S) since midnight
H = int(input())
M = int(input())
S = int(input())
# Print the angle in degrees of the hour hand on the clock face
# Note: the result is number of seconds divided by 120
# as 120 seconds is 1 degree on the clock face
print((H*3600 + M*60 + S) / 120)
