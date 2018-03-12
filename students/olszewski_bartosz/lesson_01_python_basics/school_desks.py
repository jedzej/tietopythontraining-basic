a = int(input('give kids number in class A '))
b = int(input('give kids number in class B '))
c = int(input('give kids number in class C '))
a_class = a // 2 + a % 2
b_class = b // 2 + b % 2
c_class = c // 2 + c % 2
print('desks number:', a_class + b_class + c_class)
