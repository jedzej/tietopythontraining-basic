number = int(input())

largest = 0
largest_numbers = 0

while number != 0:
    if number > largest:
        largest, largest_numbers = number, 1
    elif number == largest:
        largest_numbers += 1  
    number = int(input())
    
print(largest_numbers)
