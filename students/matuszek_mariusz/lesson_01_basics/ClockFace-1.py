H = int(input('Hours (0-12) = '))
M = int(input('Minutes (0-60) = '))
S = int(input('Seconds (0-60) = '))

print((H * 30) + (M / 2) + (S / 120))
