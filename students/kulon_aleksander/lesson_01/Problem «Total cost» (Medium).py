a = int(input())
b = int(input())
n = int(input())

d = n*a + (n*b)//100
c = (n*b)%100

print(str(d) + ' ' + str(c))