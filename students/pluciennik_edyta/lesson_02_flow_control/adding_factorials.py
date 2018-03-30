n = int(input())

result = 1
sum_of_result = 0

for n in range(1, n+1):
    result *= n
    sum_of_result += result

print(sum_of_result)
