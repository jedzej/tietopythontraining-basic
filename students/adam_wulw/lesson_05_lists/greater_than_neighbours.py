input_str = input()
input_list = input_str.split()
gtn = 0

for i in range(1, len(input_list) - 1):
    if input_list[i - 1] < input_list[i] and \
            input_list[i + 1] < input_list[i]:
        gtn = gtn + 1

print(gtn)
