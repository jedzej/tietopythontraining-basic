# script to calculate the factorial
print("enter a number")
number = int(input())

result = 1
results_added = 0
for i in range(number):
    result *= (i+1)
    results_added += result
print(str(results_added))
