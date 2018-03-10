number = int(input())

sum = number % 10
sum += number % 100 // 10
sum += number // 100

print(sum)
