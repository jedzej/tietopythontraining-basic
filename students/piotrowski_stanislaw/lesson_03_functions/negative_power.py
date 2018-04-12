# https://snakify.org/lessons/functions/problems/negative_power/
# piotrsta


def power(a, n):
    result = a ** n
    return result


if __name__ == '__main__':
    try:
        a = float(input('Enter float value: '))
        n = int(input('Enter integer value: '))
        print(power(a, n))

    except ValueError:
        print('Wrong input values.')
