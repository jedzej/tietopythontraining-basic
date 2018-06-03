from datetime import datetime
import time


timestamp = time.mktime(datetime.now().timetuple())
print("Time stamp: ", timestamp)
print("Converted timestamp: ", 
	datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d'))
