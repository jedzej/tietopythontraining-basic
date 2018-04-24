def adult(one):
    return one >= 18


def main():
    try:
        people = [int(i) for i in input().split()]
        adults = [i for i in people if adult(i)]
        kids = [i for i in people if not adult(i)]

        avg_adults_age = sum(adults) / len(adults)
        count_kids = len(kids)
        print("avg_adults_age: %f" % avg_adults_age)
        print("count_kids: %d" % count_kids)
    except ZeroDivisionError:
        print("Ooops, list cannot be empty!")


if __name__ == "__main__":
    main()
