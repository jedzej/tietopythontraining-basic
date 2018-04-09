#Statement
#Given a three-digit number. Find the sum of its digits.
print("Please enter three-digit number:")
a = int(input())
b = 0;
while a > 0:
    b += (a%10)
    a = a//10
print("Sum of digits is: " + str(b))