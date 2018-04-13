#!/usr/bin/env python3


def main():
    n = int(input())
    files = {}

    for i in range(0, n):
        file_name, *rights = input().split()
        files[file_name] = set(rights)

    m = int(input())

    for i in range(0, m):
        operation, file = [x for x in input().split()]

        if (operation == "read" and "R" in files[file] or
                operation == "write" and "W" in files[file] or
                operation == "execute" and "X" in files[file]):
            print("OK")
        else:
            print("Access denied")


if __name__ == "__main__":
    main()
