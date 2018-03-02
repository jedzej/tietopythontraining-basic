# Read an integers:
hours = int(input())
minutes = int(input())
seconds = int(input())
# Print a value:
hour_deg = 360 / 12
minute_deg = hour_deg / 60
second_deg = minute_deg / 60
total = hours * hour_deg + minutes * minute_deg + seconds * second_deg
print(total)
