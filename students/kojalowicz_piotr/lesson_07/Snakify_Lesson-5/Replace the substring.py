input_string = input()
output_string = ''
for char in input_string :
    if char != '1':
        output_string += char
    else:
        output_string += 'one'
print(output_string)
