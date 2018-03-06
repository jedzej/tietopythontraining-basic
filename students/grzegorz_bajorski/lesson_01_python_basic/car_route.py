import math

print('Enter distance which car can cover per day')
distance = int(input())

print('Enter route lenght')
lenght = int(input())

days = math.ceil (lenght / distance )
print(str(days) + ' will take to cover a route')
