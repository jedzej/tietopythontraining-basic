# Program return the second from the biggest number
# N = [1, 12, 9, 7, 8, 10]
# N = [1, 7, 9, 0]

n = int((input("put haw many elements want check:")))
N = []
i = 0

while i < n:
    print("Put", i + 1, "element:")
    l1 = int(input())
    N.append(l1)
    i += 1

i = 0
sm = 0
max1 = 0

while i < len(N):
    if (N[i]) > max1:
        a = max1
        max1 = N[i]
    if sm < N[i] < max1:
        sm = N[i]
    i += 1

if a > sm:
    sm = a

