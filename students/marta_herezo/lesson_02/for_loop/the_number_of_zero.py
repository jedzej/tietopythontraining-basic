print('Please give how many numbers you want enter: ')
n = int(input())

j = 0
for i in range(n):
    number = int(input("Enter your number: "))
    if number == 0:
        j += 1
print(j)
print('You entered ' + str(int(j)) + ' numbers of 0')
