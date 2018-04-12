all_strings = set()
for i in range(int(input('How many lines of text: '))):
    string = input('Line of text').split()
    all_strings.update(string)

print(len(all_strings))
