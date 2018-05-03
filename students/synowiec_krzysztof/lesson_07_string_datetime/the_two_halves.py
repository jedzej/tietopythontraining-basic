import math


def main():
    base_string = input()
    mid = math.ceil(len(base_string) / 2)
    interchanged = base_string[mid:] + base_string[0:mid]
    print(interchanged)


if __name__ == '__main__':
    main()
