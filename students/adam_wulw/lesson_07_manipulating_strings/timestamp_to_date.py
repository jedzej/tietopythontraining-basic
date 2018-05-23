import datetime

unix_time = int(input('Enter Unix time\n'))
time = datetime.datetime.fromtimestamp(unix_time)
print(time.strftime("%Y-%m-%d %H:%M"))
