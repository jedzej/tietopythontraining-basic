number = int(input('Number of card: '))
card = []

for i in range(0, number - 1):
    n = int(input('n: '))
    if (0 < n) and (n <= number):
        card.append(n)

for i in range(1, number + 1):
    if i not in card:
        print(i)
