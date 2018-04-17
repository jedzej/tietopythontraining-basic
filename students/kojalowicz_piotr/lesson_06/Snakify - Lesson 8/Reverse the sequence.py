n = int(input())
list_of_numbers = []
while n != 0:
    list_of_numbers.append(n)
    n = int(input())
list_of_numbers.append(n)
for i in range(len(list_of_numbers) - 1, -1, -1):
    print(list_of_numbers[i])