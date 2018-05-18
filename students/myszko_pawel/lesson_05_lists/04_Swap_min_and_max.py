# Given a list of unique numbers, swap the minimal and maximal
# elements of this list. Print the resulting list.


def main():
    numbers = [int(s) for s in input().split()]
    index_min = numbers.index(min(numbers))
    index_max = numbers.index(max(numbers))
    min_elem = numbers[index_min]
    max_elem = numbers[index_max]
    numbers[index_min] = max_elem
    numbers[index_max] = min_elem
    for i in numbers:
        print(str(i) + ' ', end='')

if __name__ == "__main__":
    main()
