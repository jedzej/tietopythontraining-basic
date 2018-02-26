#!/usr/bin/env python3

"""The `hello_world.py` approach is good for simple scripts, where the code is
unlikely to be reused.

As soon as you want to import and use your code from other modules, you want
to make sure it runs only when asked to. To do that we check magic variable
__name__, set by the interpreter. If the script has been called directly,
the variable holds '__main__' string.
"""


def main():
    print('Hello world!')


if __name__ == '__main__':
    # `python hello_world.py` will run main(), `import hello_world` will not
    main()

# `import hello_world` will still allow me to run `hello_world.main()`
