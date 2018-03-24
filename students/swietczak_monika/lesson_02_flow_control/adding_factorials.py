a = int(input("Enter a number: "))
factorial = 1
sum_of_factorials = 0
for i in range(1, a + 1):
    factorial *= i
    sum_of_factorials += factorial
print(sum_of_factorials)
