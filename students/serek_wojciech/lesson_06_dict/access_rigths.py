#!/usr/bin/env python3
"""Access rights exercise"""

ACCESS_RIGHTS = {
    'write': 'W',
    'read': 'R',
    'execute': 'X'
}


def main():
    """Main function"""
    files = {}
    for _ in range(int(input())):
        file, *perm = input().split()
        files[file] = perm

    for _ in range(int(input())):
        operation, file = input().split()
        if ACCESS_RIGHTS[operation] in files[file]:
            print("OK")
        else:
            print("Access denied")


if __name__ == '__main__':
    main()
