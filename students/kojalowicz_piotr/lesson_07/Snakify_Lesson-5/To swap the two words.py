input_string = input()
break_point = input_string.find(' ')
print(input_string[break_point + 1:] + ' ' + input_string[:break_point])
