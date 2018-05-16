from datetime import datetime

timestamp = int(input("enter timestamp: "))
print(datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S'))
