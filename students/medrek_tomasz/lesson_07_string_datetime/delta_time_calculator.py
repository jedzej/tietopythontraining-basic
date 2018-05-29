#!/usr/bin/env python3


from datetime import date


def delta_date_calculator(date_atributes):
    current_date = date.today()
    custom_date = date(**date_atributes)

    return (custom_date - current_date).days


def main():
    date_components = ['year', 'month', 'day']
    date_data = {}
    for item in date_components:
        try:
            input_number = int(input("Enter number of {} you want to"
                                     " compare with current date:\n"
                                     .format(item)))
        except ValueError:
            print("Wrong input, try again\n")

        date_data.update({item: input_number})

    print("Given date is: {} days away from now!\n"
          .format(delta_date_calculator(date_data)))


if __name__ == "__main__":
    main()
