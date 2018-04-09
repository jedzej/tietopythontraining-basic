# Negative exponent
a = float(input())
n = int(input())
def power (a, n):
    result = 1
    if n == 0:
        return 1
    for x in range (n):
        result *= a
    return result
if n < 0:
    print (power(1/a, -n))
else:
    print (power(a, n))    

