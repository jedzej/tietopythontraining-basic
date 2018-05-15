def main():
    secret_set = set(range(1, int(input("Size of range: ")) + 1))
    guess = input("Beatrice's guess (or HELP): ")
    while guess != "HELP":
        guess_set = set([int(x) for x in guess.split()])
        answer = input("August's answer: ")
        if answer == "NO":
            secret_set = secret_set.difference(guess_set)
        elif answer == "YES":
            secret_set = secret_set.intersection(guess_set)
        guess = input("Beatrice's guess (or HELP): ")

    print("List of all the remaining possible secret numbers: ")
    for x in sorted(secret_set):
        print(x, end=" ")


if __name__ == '__main__':
    main()
