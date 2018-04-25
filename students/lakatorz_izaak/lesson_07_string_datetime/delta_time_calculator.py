# write a script that calculates time difference in days between current
# date and custom date in the future.

import time


def main():

    dest_data = input("Enter data to count from: ")

    timestamp = time.mktime(time.strptime(dest_data, '%Y-%m-%d'))
    current_timestamp = int(time.time())

    timestamp_difference = abs(current_timestamp - timestamp)
    time_difference = round(timestamp_difference / 86400)
    print(time_difference)


if __name__ == "__main__":
    main()
