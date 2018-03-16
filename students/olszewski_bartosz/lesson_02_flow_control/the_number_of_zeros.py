number_of_zeros = 0
inputs = int(input())
for i in range(1, inputs + 1):
    item = int(input())
    if item == 0:
        number_of_zeros += 1
print(number_of_zeros)
