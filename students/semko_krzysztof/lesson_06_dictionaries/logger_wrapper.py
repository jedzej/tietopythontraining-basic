"""
Logger wrapper - write a function called logger_wrapper
 that wraps call to any function in order to log passed
 args. The function must take foo, *args and
 **kwargs, prints *args and **kwargs in human readable
 format and finally call foo with args and kwargs
"""


def foo(*args, **kwargs):
    print("foo():")


def logger_wrapper(func, *args, **kwargs):
    print("*args:")
    for i in args:
        print(i)
    print("**kwargs:")
    for key, val in kwargs.items():
        print(str(key) + ": " + str(val))
    
    func(args, kwargs)


def main():
    words = {'1':  'woops', '2': 'right'}
    logger_wrapper(foo, 1, 2, "hello", 'a', words, reverse=True, end='')


if __name__ == '__main__':
    main()
