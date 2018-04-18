# Given a positive real number, print its fractional part.

# Read an integer:
a = float(input())
a = str(a)
index = 0
for i in a:
    index += 1
    if(i == '.'):
        break
print('0' + a[index-1:])

###**********************###

a = float(input())
print (a-int(a))