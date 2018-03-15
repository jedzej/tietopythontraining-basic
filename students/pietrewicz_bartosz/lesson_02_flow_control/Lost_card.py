# Read the number of cards
N = int(input())
# Read the numbers on cards and calculate their sum
sum = 0
for i in range(N-1):
    sum += int(input())
# Print the number on the missing card
# The missing number is the sum of numbers on all cards minus the calculated
# sum
print((1+N)*N//2 - sum)
