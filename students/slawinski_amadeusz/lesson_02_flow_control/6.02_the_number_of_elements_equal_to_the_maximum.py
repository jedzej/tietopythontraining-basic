# find how many max numbers there are in sequence of numbers>0 ending with 0

max = 0
count = 0

while True:
    number = int(input())
    if number > max:
        max = number
        count = 1
    elif number == max:
        count += 1
    elif number == 0:
        break

print(count)
