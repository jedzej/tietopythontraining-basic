def reverse(n):
    a = input()
    if a != '0':
        n = reverse(n) + a
    return n


n = reverse('')
for i in n:
    print(i)
