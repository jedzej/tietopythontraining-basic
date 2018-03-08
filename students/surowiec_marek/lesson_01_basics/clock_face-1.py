# Read H hours, M minutes, S seconds:
H = int(input())
M = int(input())
S = int(input())
hours = H + M/60 + S/3600
# 12 hours = 360 degrees
# so X degrees = hours*360/12
# Print a value of degrees:
print(hours*360/12)
