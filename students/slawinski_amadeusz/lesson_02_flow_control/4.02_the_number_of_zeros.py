# count zeros amount number of given integers

integers = int(input())
zeros = 0

while integers:
    integers = integers - 1
    number = int(input())
    if number == 0:
        zeros = zeros + 1

print(zeros)
