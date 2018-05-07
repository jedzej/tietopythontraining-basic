numbers = [int(i) for i in input('Numbers: ').split()]

maximum = max(numbers)
minimum = min(numbers)

index_of_minimum = numbers.index(minimum)
index_of_maximum = numbers.index(maximum)
numbers[index_of_maximum] = minimum
numbers[index_of_minimum] = maximum

numbers = [str(i) for i in numbers]
print(' '.join(numbers))
