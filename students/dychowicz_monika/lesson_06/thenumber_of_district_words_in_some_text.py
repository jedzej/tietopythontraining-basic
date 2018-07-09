a = int(input())
words = set()
for i in range(a):
    line = input().split()
    for word in line:
        words.add(word)
print(len(words))
def dist_word():
    a = int(input("Enter number of lines: "))
    words = set()
    for i in range(a):
        line = input("Enter words: ").split()
        for word in line:
            words.add(word)
    print("Number of words in entered lines:")
    print(len(words))


if __name__ == "__main__":
    dist_word()