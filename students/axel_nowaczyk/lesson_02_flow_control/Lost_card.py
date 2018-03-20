def lost_card():
    card_count = int(input())
    inputs = []
    while len(inputs) < (card_count - 1):
        inp = int(input())
        inputs.append(inp)
    sorted_inputs = sorted(inputs)
    for i in range(1,card_count):
        if i != sorted_inputs[i-1]:
            print(i)
            return 
    print(card_count)


if __name__ == '__main__':
    lost_card()