import datetime

raw_data = input('year days hours minutes\n')
in_data = list(map(int, raw_data.split(' ')))

time_to_add = datetime.timedelta(days=in_data[0] * 365 + in_data[1],
                                 hours=in_data[2], minutes=in_data[3])

now = datetime.datetime.now()
result = now + time_to_add

print(result.strftime("%Y-%m-%d %H:%M"))
