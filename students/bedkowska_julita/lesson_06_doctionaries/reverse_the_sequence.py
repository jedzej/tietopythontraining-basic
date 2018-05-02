print('Input numbers:')
input_num = ''
number = ''
while input_num != '0':
    input_num = input()
    number += input_num
print('Result:')
for i in range(len(number)):
    print(number[len(number) - i - 1])
