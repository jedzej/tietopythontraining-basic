import time
import datetime

timestamp = time.time()
value = datetime.datetime.fromtimestamp(timestamp)

print(value.strftime('%Y-%m-%d %H:%M:%S'))
