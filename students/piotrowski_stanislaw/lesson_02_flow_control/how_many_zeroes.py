#https://snakify.org/lessons/for_loop_range/problems/how_many_zeroes/
#piotrsta

number_of_numbers = int(input())
zeros = 0

for i in range(number_of_numbers):
    number = int(input())
    if number == 0:
        zeros += 1
print(zeros)
