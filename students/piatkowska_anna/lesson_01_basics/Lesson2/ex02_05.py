#Statement
#Given a positive real number, print its first digit to the right of the decimal point.
print("Please enter a positive real number:")
a = float(input())
a = (a-int(a))*10
print("First digit to the right of the decimal point is: " +  str(int(a)))