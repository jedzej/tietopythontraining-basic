from math import sqrt

def main():
    x1 = float(input())
    y1 = float(input())
    x2 = float(input())
    y2 = float(input())
    print(distance(x1,y1,x2,y2))

def distance(x1,y1,x2,y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

if __name__ == '__main__':
    main()
