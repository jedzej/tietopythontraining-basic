
def sum_digits():
    a = input()
    digits = map(lambda x: int(x), list(a))
    print(sum(digits))


if __name__ == '__main__':
    sum_digits()