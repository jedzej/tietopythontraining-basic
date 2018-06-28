def inspect_args(*args, **kwargs):
    for arg in args:
        print("Passed argument: " + str(arg) +
              " is type of: " + str(type(arg)))
    for arg in kwargs:
        print("Passed argument: " + str(arg) +
              " is type of: " + str(type(arg)))


if __name__ == '__main__':
    inspect_args({'gold coin': 42, 'rope': 1},
                 ["era", "plus"],
                 (1, 2, 3),
                 1, 2, 3.5,
                 "Balon",
                 USA='New York')
