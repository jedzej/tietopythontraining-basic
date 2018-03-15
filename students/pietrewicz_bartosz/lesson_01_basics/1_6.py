# Read the number of students in 3 classes
a = int(input())
b = int(input())
c = int(input())
# Print the minimal number of desks the school must purchase
desks_a = a//2 + a % 2
desks_b = b//2 + b % 2
desks_c = c//2 + c % 2
print(desks_a + desks_b + desks_c)
