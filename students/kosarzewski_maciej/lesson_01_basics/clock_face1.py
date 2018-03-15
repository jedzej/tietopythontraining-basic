# Read an integers:
hours = int(input("Hour: "))
minutes = int(input("Minute: "))
seconds = int(input("Second: "))
# Print a value:
hour_deg = 360 / 12
minute_deg = hour_deg / 60
second_deg = minute_deg / 60
total = hours * hour_deg + minutes * minute_deg + seconds * second_deg
print(total)

