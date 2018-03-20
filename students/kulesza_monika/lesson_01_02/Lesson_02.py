def minimum_of_two_numbers():
    a = int(input())
    b = int(input())

    if a > b:
        print (b)
    else:
        print (a)

#######################################################

def sign_function():
    a = int(input())

    if a > 0:
        print (1)
    elif a < 0:
        print (-1)
    else:
        print (0)

#######################################################

def minimum_of_three_numbers():
    a = int(input())
    b = int(input())
    c = int(input())

    list = [a, b, c]
    print (min(list))

#######################################################

def equal_numbers():
    a = int(input())
    b = int(input())
    c = int(input())

    if a == b and b == c:
        print (3)
    elif a == b or b == c or a == c:
        print (2)
    else:
        print (0)

#######################################################

def rook_move():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())

    if c == a or d == b:
        print ("YES")
    else:
        print ("NO")

#######################################################

def chess_board():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    # black
    if a % 2 == 1 and b % 2 == 1 and c % 2 == 0 and d % 2 == 0:
        print('YES')
    elif a % 2 == 1 and b % 2 == 1 and c % 2 == 1 and d % 2 == 1:
        print('YES')
    elif a % 2 == 0 and b % 2 == 0 and c % 2 == 0 and d % 2 == 0:
        print('YES')
    elif a % 2 == 0 and b % 2 == 0 and c % 2 == 1 and d % 2 == 1:
        print('YES')
    # white
    elif a % 2 == 0 and b % 2 == 1 and c % 2 == 0 and d % 2 == 1:
        print('YES')
    elif a % 2 == 1 and b % 2 == 0 and c % 2 == 1 and d % 2 == 0:
        print('YES')
    elif a % 2 == 0 and b % 2 == 1 and c % 2 == 1 and d % 2 == 0:
        print('YES')
    elif a % 2 == 1 and b % 2 == 0 and c % 2 == 0 and d % 2 == 1:
        print('YES')
    else:
        print('NO')

#######################################################

def king_move():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())

    if c == (a - 1) and d == (b + 1):
        print ("YES")
    elif c == a and d == (b + 1):
        print ("YES")
    elif c == (a + 1) and d == (b + 1):
        print ("YES")
    elif c == (a - 1) and d == b:
        print ("YES")
    elif c == (a + 1) and d == b:
        print ("YES")
    elif c == (a - 1) and d == (b - 1):
        print ("YES")
    elif c == a and d == (b - 1):
        print ("YES")
    elif c == (a + 1) and d == (b - 1):
        print ("YES")
    else:
        print ("NO")

#######################################################

reszty szach nie robie, wszystko na jedno kopyto jest

#######################################################

def chocolate_bar():
    n = int(input())
    m = int(input())
    k = int(input())

    if (n * m) >= k:
        if (k % n == 0) or (k % m == 0):
            print ("YES")
        else:
            print ("NO")
    else:
        print ("NO")

#######################################################

def leap_year():
    a = int(input())

    if a % 400 == 0:
        print ("LEAP")
    elif a % 100 == 0:
        print ("COMMON")
    elif a % 4 == 0:
        print ("LEAP")
    else:
        print ("COMMON")

#######################################################

def sec_max():
    lista = []

    while True:
        try:
            a = int(input())
            lista.append(a)
        except Exception:
            break
    lista.sort()
    print(lista[-2])

#######################################################

def elem_max():
    lista = []

    while True:
        try:
            a = int(input())
            lista.append(a)
        except Exception:
            break
    print (lista.count(max(lista)))












