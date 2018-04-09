numbers = input('Numbers: ').split()

counter = 0
for loop in range(1, len(numbers) - 1):
    if numbers[loop] > numbers[loop - 1] and numbers[loop] > numbers[loop + 1]:
        counter += 1

print(counter)
