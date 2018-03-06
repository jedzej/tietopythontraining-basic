#!/usr/bin/env python3
"""Apple sharing"""


def main():
    """Main function"""
    students = int(input())
    apples = int(input())

    print(apples // students)   # apples per student
    print(apples % students)    # remaining apples


if __name__ == '__main__':
    main()
