
def print_number_of_hours_and_minutes():

    number_of_minutes = int(input("Provide number o minutes "))

    hours = int(number_of_minutes/60)
    minutes = number_of_minutes % 60

    print(str(hours) + ":" + str(minutes))


print_number_of_hours_and_minutes()
