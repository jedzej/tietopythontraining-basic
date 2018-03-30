
def calculate_number_of_zeroes():

    counter = 0

    for i in range(int(input())):
        if int(input()) == 0:
            counter += 1

    print(counter)


calculate_number_of_zeroes()
