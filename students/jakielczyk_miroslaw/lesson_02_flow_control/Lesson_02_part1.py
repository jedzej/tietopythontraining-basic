# Bishop moves
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a >= 1 and b >= 1 and c >= 1 and d >= 1 and a <= 8 and b <= 8 and c <= 8 and d <= 8:
    if c-a == d-b or a-c == d-b :
        print ("YES")
    else:
        print ("NO")
else :
    print ("NO")


# Queen move
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a >= 1 and b >= 1 and c >= 1 and d >= 1 and a <= 8 and b <= 8 and c <= 8 and d <= 8:
    if (c-a == d-b or a-c == d-b) or (c-a == 0 and d-b != 0) or (d-b == 0 and c-a != 0): 
        print ("YES")
    else:
        print ("NO")
else :
    print ("NO")

    
# Knight move
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a >= 1 and b >= 1 and c >= 1 and d >= 1 and a <= 8 and b <= 8 and c <= 8 and d <= 8:
    if ((c-a == 1 or a-c == 1) and (d-b == 2 or b-d == 2)) or ((c-a == 2 or a-c == 2) and (d-b == 1 or b-d == 1)):
        print ("YES")
    else:
        print ("NO")
else :
    print ("NO")

    
# Chocolate bar
n = int(input())
m = int(input())
k = int(input())
if (k%n == 0 and k//n <= m) or (k%m == 0 and k//m <= n):
    print ("YES")
else:
    print ("NO")


# Leap year
a = int(input())
if a%400 == 0 :
    print ("LEAP")
elif a%4 == 0 and a%100 != 0 :
    print ("LEAP")
else :
    print ("COMMON")

