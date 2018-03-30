print("Digital clock\n")

a = int(input("Enter the number of minutes: "))

h = a // 60
m = a % 60

print("\nIt is " + str(h) + " " + str(m))