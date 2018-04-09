number = int(input())
biggest = 0
numbers_list = []
# Print a value:
while number != 0:
    if number >= biggest:
        biggest = number
        numbers_list.append(number)
    number = int(input())
print(numbers_list.count(biggest))
