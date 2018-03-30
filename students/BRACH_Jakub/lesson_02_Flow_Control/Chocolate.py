n = int(input())
m = int(input())
k = int(input())

if (k % n == 0 and m >= (k // n)) or (k % m == 0 and n > k // m):
    print("YES")
else:
    print("NO")
