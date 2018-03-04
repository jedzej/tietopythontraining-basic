# Read an integer:
h = int(input("enter hours: "))
m = int(input("enter minutes: "))
s = int(input("enter seconds: "))

angle = 0.5 * (60 * h + m + s / 60)
print(angle)
