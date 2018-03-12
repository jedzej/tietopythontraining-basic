
def print_degree_of_hour_hand():

    h = int(input("Provide number of hours "))
    m = int(input("Provide number of minutes "))
    s = int(input("Provide number of seconds "))

    print(h * 30 + m * 30 / 60 + s * 30 / 3600)


print_degree_of_hour_hand()
