N = int(input("N: "))
all_sum = 0
cards_sum = 0
for i in range(1, N + 1):
    all_sum += i
    if i < N:
        cards_sum += int(input("Cards: "))
print(all_sum - cards_sum)
