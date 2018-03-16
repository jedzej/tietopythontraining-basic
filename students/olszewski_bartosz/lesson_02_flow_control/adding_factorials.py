j = 1
sum_of_numbers = 0
factorial = 1
user_input = int(input())
for i in range(1, user_input + 1):
    factorial *= i
    if i == j:
        sum_of_numbers = sum_of_numbers + factorial
        j += 1
print(sum_of_numbers)
