number_of_lines = int(input())
unique_words = set()
for lines in range(number_of_lines):
    unique_words.update(input().split())
print(len(unique_words))
