# Date printer - write a script that displays current date in human-readable
#  format.
import datetime


def main():

    current_data = datetime.datetime.now()
    print(current_data.strftime("%Y-%m-%d"))


if __name__ == "__main__":
    main()
