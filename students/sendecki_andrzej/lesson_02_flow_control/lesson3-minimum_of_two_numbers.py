import sys

print("Input the first number:")
a=input()
print("Input the second number:")
b=input()
if a == b:
    print("numbers are equal")
    sys.exit()

print("The smaller number is:")
if a < b:
    print(a)
else:
    print(b)
