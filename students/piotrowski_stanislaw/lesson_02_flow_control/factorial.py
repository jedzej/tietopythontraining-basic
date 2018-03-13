#https://snakify.org/lessons/for_loop_range/problems/factorial/
#piotrsta

number = int(input())
factorial = 1

for i in range(1, number + 1):
    factorial *= i
print(factorial)
