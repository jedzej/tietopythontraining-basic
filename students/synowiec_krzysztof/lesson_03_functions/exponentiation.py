def main():
    a = float(input())
    n = int(input())
    print(power(a,n))

def power(a,n):
    if (n == 0):
        return 1
    else:
        return a * power(a, n-1)

if __name__ == '__main__':
    main()
