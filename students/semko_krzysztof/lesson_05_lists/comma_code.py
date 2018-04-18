"""
Say you have a list value like this:

spam = ['apples', 'bananas', 'tofu', 'cats']

Write a function that takes a list value as an argument
and returns a string with all the items separated
by a comma and a space, with and inserted before
the last item. For example, passing the previous
spam list to the function would
return 'apples, bananas, tofu, and cats'.
But your function should be able to work
with any list value passed to it.
"""


def transform_string(collection):
    string = ""
    collection.insert(-1, 'and')
    for i in range(len(collection)):
        if len(collection) - i > 2:
            string += collection[i] + str(", ")
        elif len(collection) - i == 2:
            string += collection[i] + str(" ")
        elif len(collection) - i == 1:
            string += collection[i]

    return string


def main():
    spam = ['apples', 'bananas', 'tofu', 'cats']
    print(transform_string(spam))


if __name__ == '__main__':
    main()
