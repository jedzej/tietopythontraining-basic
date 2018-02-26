import math

def minDeskNumber(numberOfStudents):
    return math.ceil(numberOfStudents/2)

def main():

    aClassDesks = minDeskNumber(int(input()))
    bClassDesks = minDeskNumber(int(input()))
    cClassDesks = minDeskNumber(int(input()))
    print(aClassDesks + bClassDesks + cClassDesks)

if __name__ == '__main__':
    main()