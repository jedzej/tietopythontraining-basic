hours = int(input('Hours: '))
minutes = int(input('Minutes: '))
seconds = int(input('Seconds: '))

hourAngle = 360/12
minuteAngle = (360/12)/60
secondAngle = ((360/12)/60)/60

angle = hours * hourAngle + minutes * minuteAngle + seconds * secondAngle
print(angle)

