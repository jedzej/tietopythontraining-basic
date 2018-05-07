n = int(input("Highest number: "))
sum = 0
max = 0
for i in range(1, n + 1):
    sum += i
for j in range(1, n):
    card = int(input("Card number:"))
    sum -= card
print(sum)
