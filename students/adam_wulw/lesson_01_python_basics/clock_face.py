h = int(input('Enter hours\n'))
m = int(input('Enter minutes\n'))
s = int(input('Enter seconds\n'))
total_sec = h * 3600 + m * 60 + s
print('The angle of haur hand is ' + str(total_sec / 120))
