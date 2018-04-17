def inspect_kwargs(**kwargs):
    for key, value in kwargs.items():
        print("This is my {} - {}".format(key, value))

inspect_kwargs(
              Name="Martin",
              Surname="Tomson",
              Age=10
)


def inspect_args(*args):
    sum_of_numbers = 0
    for eachNumber in args:
        sum_of_numbers += eachNumber
    print("This is the sum: " + str(sum_of_numbers))

inspect_args(4, 5, 6, 7, 8)
