from math import ceil


def car_route():
    n = int(input())
    m = int(input())

    if n == 0:
        print("inf")
    else:
        print(ceil(m/n))


if __name__ == '__main__':
    car_route()