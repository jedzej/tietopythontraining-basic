# https://snakify.org/lessons/for_loop_range/problems/sum_of_factorials/
# piotrsta

number = int(input())
factorial = 1
sum_of_factorials = 0

for i in range(1, number + 1):
    factorial *= i
    sum_of_factorials += factorial
print(sum_of_factorials)
