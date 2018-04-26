

def main():
    ages = [int(x) for x in input().split()]
    adults = [x for x in ages if x >= 18]
    print("Avg. adults age:", sum(adults) / len(adults))
    print("Children count:", len(ages) - len(adults))


if __name__ == '__main__':
    main()
