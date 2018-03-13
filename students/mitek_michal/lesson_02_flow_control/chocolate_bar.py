
def divide_chocolate_bar():

    n = int(input("Provide n portions "))
    m = int(input("Provide m portions "))
    k = int(input("Provide squares "))

    if k <= n * m and (k % n == 0 or k % m == 0):
        print('YES')
    else:
        print('NO')


divide_chocolate_bar()
