#Statement
#H hours, M minutes and S seconds are passed since the midnight 
#(0 ≤ H < 12, 0 ≤ M < 60, 0 ≤ S < 60). 
#Determine the angle (in degrees) of the hour hand on the clock face right now.
print("Enter hours (0 ≤ H < 12):")
a = int(input())
print("Enter minutes (0 ≤ M < 60):")
b = int(input())
print("Enter seconds (0 ≤ S < 60):")
c = int(input())
print("The angle (in degrees) of the hour hand on the clock face is: " + str(((a*3600+b*60+c)*360)/43200))