def main():
    a = float(input())
    n = int(input())
    print(power(a,n))

def power(a,n):
    if (n < 0):
        n = -n
        a = 1/a
    result = 1
    for x in range(0, n):
        result *= a
    return result

if __name__ == '__main__':
    main()
