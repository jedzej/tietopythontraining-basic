num = int(input('Enter the number\n'))
sum = (num % 10) + ((num % 100) // 10) + ((num % 1000) // 100)
print('The sum of digits is ' + str(sum))

