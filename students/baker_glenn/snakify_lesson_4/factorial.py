# script to calculate the factorial
print("enter a number")
number = int(input())

result = 1
for i in range(number):
    result *= (i+1)
print(str(result))
