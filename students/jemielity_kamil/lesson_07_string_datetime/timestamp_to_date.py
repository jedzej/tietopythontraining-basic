from datetime import datetime

seconds = float(input('Unix timestamp: '))
print(datetime.fromtimestamp(seconds).strftime("%d-%m-%Y %H:%M:%S"))
