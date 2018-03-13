# Read an integer:
# a = int(input())
# Print a value:
# print(a)
# oszukałem w tym zadaniu i pomagało mi google 

n = int(input())
card = 0
for i in range(1, n+1):
    card += i

for i in range(n-1):
    card -= int(input())

print(card)