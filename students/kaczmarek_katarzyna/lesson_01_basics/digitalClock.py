numberOfMinutes = int(input("Number of minutes: "))
numberOfMinutes = numberOfMinutes % 1440

print(numberOfMinutes // 60, numberOfMinutes % 60)
