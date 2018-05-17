# Timestamp to date - write a script that converts unix timestamp to
# human-readable date format
import time
import datetime


def main():

    timestamp = time.time()
    print('Timestamp: ' + str(timestamp))
    my_data = datetime.datetime.fromtimestamp(timestamp)
    print(my_data.strftime("%Y-%m-%d"))


if __name__ == "__main__":
    main()
