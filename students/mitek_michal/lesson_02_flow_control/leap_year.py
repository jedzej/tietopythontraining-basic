
def check_if_year_is_leap():

    year = int(input("Provide a year"))

    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print('LEAP')
    else:
        print('COMMON')


check_if_year_is_leap()
