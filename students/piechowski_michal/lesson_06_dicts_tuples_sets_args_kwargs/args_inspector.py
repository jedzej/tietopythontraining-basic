#!/usr/bin/env python3


def inspect_args(*args, **kwargs):
    print("Positional arguments:")
    for arg in args:
        print("- " + str(arg))
    print("")
    print("Keyword arguments:")
    for keyword, value in kwargs.items():
        print("- " + str(keyword) + " : " + str(value))


def main():
    inspect_args(4, "arg", [2, 7, 5], key_word_arg=True, some_string="Hello")


if __name__ == "__main__":
    main()
