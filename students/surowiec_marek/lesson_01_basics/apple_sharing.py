# Read the numbers students and apples counts:
students_count = int(input())
apples_count = int(input())
print(str(apples_count//students_count) + ' apples will get each single student')
print(str(apples_count%students_count) + ' apples will remain in the basket')
