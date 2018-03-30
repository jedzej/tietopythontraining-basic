def get_lost_card():
    maximum_card = int(input())
    sum_of_cards = 0

    for i in range(1, maximum_card + 1):
        sum_of_cards += i

    for i in range(maximum_card - 1):
        sum_of_cards -= int(input())

    lost_card = sum_of_cards
    print(lost_card)


if __name__ == '__main__':
    get_lost_card()
