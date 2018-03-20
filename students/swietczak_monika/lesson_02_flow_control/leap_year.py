# Read an integer:
year = int(input("Enter a year: "))
# Print a value:
if year % 4 == 0 and not year % 100 == 0:
    print("LEAP")
elif year % 400 == 0:
    print("LEAP")
else:
    print("COMMON")
