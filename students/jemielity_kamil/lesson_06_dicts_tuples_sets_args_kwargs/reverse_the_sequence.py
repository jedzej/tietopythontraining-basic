def reverse_the_sequence(*args):
    if len(args) is not 0:
        print(args[-1])
        reverse_the_sequence(*args[0:-1])


reverse_the_sequence(1, 2, 3, 4, 5, 0)
