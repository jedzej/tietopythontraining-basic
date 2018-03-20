# Given a positive real number, print its first digit to the right of the decimal point.

# Read an integer:
a = float(input())
a = str(a)
index = 0
for i in a:
    index += 1
    if(i == '.'):
        break
print(a[index])