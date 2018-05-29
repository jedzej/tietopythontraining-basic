import datetime

raw_data = input('year month day\n')
in_data = list(map(int, raw_data.split(' ')))

now = datetime.date.today()
future_time = datetime.date(in_data[0], in_data[1], in_data[2])

result = future_time - now
print(result.days)
