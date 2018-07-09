#Given a list of numbers, determine and print the quantity of elements that are greater than both of their neighbors.
#The first and the last items of the list shouldn't be considered because they don't have two neighbors. 


numbers = [1, 2, 6, 4, 5, 6, 2, 8, 1, 0, 1, -9]
has_neighbours = 0

for i in range(1, len(numbers) - 1):
    if numbers[i-1] < numbers[i] > numbers[i+1]:
        has_neighbours += 1

print(has_neighbours)
