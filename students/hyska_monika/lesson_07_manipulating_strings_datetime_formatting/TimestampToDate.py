# Timestamp to date
# script converts unix timestamp to human-readable date format
import time
import datetime

unix_date = (time.time())
print(unix_date)
print(datetime.datetime.fromtimestamp(int(unix_date)).
      strftime('%d.%m.%Y %H:%M:%S'))
