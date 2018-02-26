def main():
    anglePerSecond = (3600 * 12)/360
    hours = int(input())
    minutes = int(input())
    seconds = int(input())
    totalSeconds = hours * 3600 + minutes * 60 + seconds
    angle = totalSeconds / anglePerSecond
    print(angle)

if __name__ == '__main__':
    main()