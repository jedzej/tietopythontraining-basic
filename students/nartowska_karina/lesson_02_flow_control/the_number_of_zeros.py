zeros = 0
amount = int(input())
for i in range(0, amount):
    value = int(input())
    if value == 0:
        zeros += 1
print(zeros)
