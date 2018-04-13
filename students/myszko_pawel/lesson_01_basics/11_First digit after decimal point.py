# Given a positive real number, print its first digit to the right of the decimal point.

a = float(input())
a = str(a)
index = 0
for i in a:
    index += 1
    if(i == '.'):
        break
print(a[index])

###*******************###

a = float(input())
a = a - int(a)
a = str(a)[2]
print(a)
