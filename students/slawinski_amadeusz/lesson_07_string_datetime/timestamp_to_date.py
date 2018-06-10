#!/urs/bin/env python3

import datetime

timestamp = input()

time = datetime.datetime.fromtimestamp(int(timestamp))

print(time.strftime("%H:%M %d.%m.%Y"))
