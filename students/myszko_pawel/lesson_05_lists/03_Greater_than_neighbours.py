# Given a list of numbers, determine and print the quantity of elements that are greater than both of their neighbors.
# The first and the last items of the list shouldn't be considered because they don't have two neighbors.

def main():

    numbers = [int(s) for s in input().split()]
    quantity = 0
    for i in range (1, len(numbers) - 1):
        if numbers[i-1] < numbers[i] > numbers[i+1]:
            quantity += 1
    print(quantity)

if __name__ == "__main__":
    main()
