def collatz(number):
    tmp = number % 2
    if tmp:
        tmp = 3 * number + 1
    else:
        tmp = number // 2
    print(tmp)
    return tmp


def main():
    print("Provide input")
    try:
        number = int(input())
        while number != 1:
            number = collatz(number)
    except ValueError:
        print("Must use an integer!")


if __name__ == '__main__':
    # `python hello_world.py` will run main(), `import hello_world` will not
    main()
