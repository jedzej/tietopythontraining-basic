def collatz(number):
    if number % 2 == 0:
        temp_value = number // 2
        print(temp_value)
        return temp_value
    else:
        temp_value = 3 * number + 1
        print(temp_value)
        return temp_value


def main():
    while True:
        input_value = int(input())
        if collatz(input_value) == 1:
            print("End")
            break


if __name__ == '__main__':
    main()
