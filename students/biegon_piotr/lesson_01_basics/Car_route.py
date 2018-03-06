import math
print("Car route\n")

N = int(input("Enter the number of kilometers that a car can drive in one day: "))
M = int(input("Enter the length of the route in kilometers: "))

a = math.ceil(M / N)

print("\nCrossing the route with a length of %d kilometers will take %d days" %(M, a))