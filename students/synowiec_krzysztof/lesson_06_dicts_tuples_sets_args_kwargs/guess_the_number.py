def main():
    secret_set = set(range(1, int(input()) + 1))
    guess = input()
    while guess != "HELP":
        guess_set = set([int(x) for x in guess.split()])
        answer = input()
        if answer == "NO":
            secret_set = secret_set.difference(guess_set)
        elif answer == "YES":
            secret_set = secret_set.intersection(guess_set)
        guess = input()

    for x in secret_set:
        print(x, end=" ")


if __name__ == '__main__':
    main()
