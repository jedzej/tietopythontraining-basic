# Date calculator - write a script that adds custom number of years,
# days and hours and minutes to current date and displays the result in
# human readable format.
import time
import datetime


def main():

    print('Enter years, days, hours and minutes you want to add.')
    years, days, hours, mins = [int(x) for x in input().split(' ')]
    add_value = (years * 31536000
                 + days * 86400
                 + hours * 3600
                 + mins * 60)

    timestamp = time.time()
    my_data = datetime.datetime.fromtimestamp(timestamp + add_value)
    print(my_data.strftime("%Y-%m-%d  %H:%M"))


if __name__ == "__main__":
    main()
