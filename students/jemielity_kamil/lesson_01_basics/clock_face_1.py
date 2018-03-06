hours = int(input('Hours: '))
minutes = int(input('Minutes: '))
seconds = int(input('Seconds: '))

hour_angle = 360/12
minute_angle = (360/12)/60
second_angle = ((360/12)/60)/60

angle = hours * hour_angle + minutes * minute_angle + seconds * second_angle
print(angle)
