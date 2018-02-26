import math

def main():
    distancePerDay = int(input())
    distnce = int(input())
    numberOfDays = math.ceil(distnce/distancePerDay)
    print(numberOfDays)

if __name__ == '__main__':
    main()