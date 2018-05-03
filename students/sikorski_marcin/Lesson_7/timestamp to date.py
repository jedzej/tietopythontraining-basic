import datetime, time
currentTime = time.time()

def converter_of_unix_time(stamp):
    value = datetime.datetime.fromtimestamp(stamp)
    print(value.strftime('%Y-%m-%d %H:%M:%S'))

converter_of_unix_time(currentTime)