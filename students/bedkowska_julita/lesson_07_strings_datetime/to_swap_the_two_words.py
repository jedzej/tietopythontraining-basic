text = input('Input the text: ')
space_index = text.find(' ')
swaped_text = text[space_index + 1:] + ' ' + text[:space_index]
print('The swaped text: ' + swaped_text)
