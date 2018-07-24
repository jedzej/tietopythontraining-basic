from datetime import datetime
import time


timestamp = time.mktime(datetime.now().timetuple())
time = datetime.fromtimestamp(timestamp)
print("Time stamp: ", timestamp)
print("Converted timestamp: ", time.strftime('%Y-%m-%d'))
