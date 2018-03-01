import math
N = int(input('How many minutes: '))

hours = math.floor(N/60)
minutes = N-(hours*60)
print(str(hours) + " " + str(minutes))

