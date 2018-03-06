print('Enter hour')
hour = int(input())

print('Enter minutes')
minutes = int(input())

print('Enter seconds')
seconds = int(input())

angle = float(hour *30) + float(minutes * 0.5) + float(seconds * (30/3600))

print('Angle is ' + str(angle))
