# calculate the degree of the hour hand
degree_for_1_min = (360 / 12) / 60
degree_for_1_sec = degree_for_1_min / 60
print("enter the hours")
hour = int(input())
print("enter the minutes")
minute = int(input())
print("enter the seconds")
second = int(input())
print("the hour hand degree is " + str((hour * 30) + (degree_for_1_min * minute) + (degree_for_1_sec * second)))

