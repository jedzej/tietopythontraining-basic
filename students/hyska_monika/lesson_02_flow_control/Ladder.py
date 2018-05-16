# Program print leader from numbers

n = int((input("put haw many layer leader should have(put from 1 to 9):")))
a = 1
print(1)

for i in range(2, n + 1):
    a = str(a) + str(i)
    print(a, sep='')
