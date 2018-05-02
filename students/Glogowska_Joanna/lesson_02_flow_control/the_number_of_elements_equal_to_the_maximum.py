max = 0
end = 0
i = int(input('Write integers, end the sequence with 0'))
while i != 0:
    if i > max:
        max = i
        end = 0
    if i == max:
        end += 1
    i = int(input())
print('Number of elements equal to max is ' + str(end))
