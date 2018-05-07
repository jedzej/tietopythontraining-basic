# Numbers filter - using list comprehensions write a function that casts
# list of strings to list of integers and filters numbers within supplied
# range. Example data:


def cast_to_int(user_list, user_range):
    list_of_integers = [int(value) for value in user_list]
    filtered_integers = [
        value for value in list_of_integers if value not in range(user_range)]

    return filtered_integers


def main():
    list_of_strings = ['1', '2', '0', '8', '3']

    output = cast_to_int(list_of_strings, 3)
    print(output)


if __name__ == "__main__":
    main()
