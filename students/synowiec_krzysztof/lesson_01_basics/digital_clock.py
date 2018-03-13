def main():
    minutesFromMidnight = int(input())
    minutsPerDay = 24 * 60
    reducedMinutes = minutesFromMidnight % minutsPerDay
    hours = reducedMinutes // 60
    minutes = reducedMinutes % 60
    print("{0} {1}".format(hours, minutes))

if __name__ == '__main__':
    main()
