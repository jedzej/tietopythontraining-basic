def reverse():
    user_input = int(input())
    if user_input != 0:
        reverse()
    print(user_input)


def main():
    reverse()


if __name__ == '__main__':
    main()
