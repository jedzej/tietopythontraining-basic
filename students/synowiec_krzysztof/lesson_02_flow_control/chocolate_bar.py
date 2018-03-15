def main():
    m = int(input())
    n = int(input())
    k = int(input())
    max = m*n

    if (k % m == 0  or k % n == 0) and k < max:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()
