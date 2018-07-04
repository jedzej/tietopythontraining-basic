from datetime import date


if __name__ == '__main__':
    timestampt = int(input("Enter unix timestamp: "))
    print("Today is: ")
    print(date.fromtimestamp(timestampt))
