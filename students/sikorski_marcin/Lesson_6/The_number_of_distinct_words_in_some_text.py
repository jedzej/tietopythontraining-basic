unique_words = set()

for word in range(int(input("How many lines"))):
    unique_words.update(input("Type the lines, dummy!: ").split())
print(len(unique_words))
