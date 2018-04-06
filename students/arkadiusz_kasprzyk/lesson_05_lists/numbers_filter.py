def numbers_filter(numbers, range):
    return [int(s) for s in numbers if int(s) not in range]

numbers = ['1', '2', '0', '8', '3']
range = range(3)
print(numbers_filter(numbers, range))