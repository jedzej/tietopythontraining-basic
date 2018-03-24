
def determine_lost_card():

    n = int(input("Provide number of cards "))
    sum_cards = 0

    for i in range(1, n + 1):
        sum_cards += i

    for i in range(n - 1):
        sum_cards -= int(input("Provide next card "))
    print(sum_cards)


determine_lost_card()
