#https://snakify.org/lessons/print_input_numbers/problems/apple_sharing/
#piotrsta

print('Ilu uczniow: ')
n = int(input())
print('Ile jablek: ')
k = int(input())

applesPerStud=k//n
print('Uczen dostanie '+str(applesPerStud)+' jablek')
remainInBasket=k%n
print('W koszu zostanie '+str(remainInBasket)+' jablek')

