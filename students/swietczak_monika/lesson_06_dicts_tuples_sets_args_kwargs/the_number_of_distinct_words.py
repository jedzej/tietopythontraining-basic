set_of_words = set()
n = int(input("Enter number of lines: "))
for i in range(n):
    text = input("Enter some text: ").split()
    for word in text:
        if word not in set_of_words:
            set_of_words.add(word)

print(len(set_of_words))
