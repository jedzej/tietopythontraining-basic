
def collatz(number):

    try:
        if number % 2 == 0:
            result = number // 2
            print(result)

            return result

        elif number % 2 == 1:
            result = 3 * number + 1
            print(result)

            return result

    except TypeError:
        print("Wrong input :(")
