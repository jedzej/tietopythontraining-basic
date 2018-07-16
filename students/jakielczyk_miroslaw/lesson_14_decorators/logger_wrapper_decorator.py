import sys
import logging
sys.path.append('..')
from lesson_06_dicts_tuples_sets_args_kwargs import logger_wrapper


def test_function(*args, **kwargs):
    print("\nArgs & Kwargs provided for called function:")
    summary = 0
    for argument in args:
        summary += argument
        print(argument)
    print("\nKey =>  Value")
    for key in kwargs:
        print(key, "=>", kwargs[key])
    return summary


def logger_wrapper_decorator(func):
    def func_wrapper(function_name, *args, **kwargs):
        correct_arguments = True
        for argument in args:
            if not isinstance(argument, (int, float)):
                correct_arguments = False
                logging.error('Incorrect type of argument {} {}'.format(argument, type(argument)))
        if correct_arguments:
            logging.debug('Called function -> {}'.format(function_name))
            return func(function_name, *args, **kwargs)
    return func_wrapper


@logger_wrapper_decorator
def logger_wrapper_dec(function_name, *args, **kwargs):
    return logger_wrapper.logger_wrapper(function_name, *args, **kwargs)


def main():
    logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

    logger_wrapper_dec(test_function, 2.8, 6, 30, 13, brand="Volkswagen",
                       car="Polo", year=2002, power=105)

    logger_wrapper_dec(test_function, 2.8, 'abcd', 6, 30, 13, brand="Opel",
                       car="Astra", year=2012, power=120)


if __name__ == "__main__":
    main()
