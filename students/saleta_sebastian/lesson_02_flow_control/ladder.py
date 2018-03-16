from __future__ import print_function

def print_ladder():
    maxium_step = int(input())

    for i in range(1, maxium_step + 1):
        for j in range(1, i + 1):
            print(j, sep='', end='')
        print()


if __name__ == '__main__':
    print_ladder()