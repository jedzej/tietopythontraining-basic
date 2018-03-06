a = int(input('give a number '))
a = a % 1440
hours = a // 60
minutes = a - hours * 60
print('hour on the digital clock', hours, ':', minutes)
# print('hour on the digital clock {}:{}'.format(hours, minutes))
