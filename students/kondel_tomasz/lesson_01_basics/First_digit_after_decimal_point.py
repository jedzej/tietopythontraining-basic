a = input()
b = a.split('.')
if len(b) > 1:
    c = b[1]
    print(c[0])
else:
    print(0)
