import math
n = int(input('How many minutes: '))

hours = math.floor(n/60)
minutes = n-(hours*60)
print(str(hours) + " " + str(minutes))

