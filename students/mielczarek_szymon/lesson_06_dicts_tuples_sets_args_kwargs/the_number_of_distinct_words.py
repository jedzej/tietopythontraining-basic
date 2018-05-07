number_of_lines = int(input())
words = set()
for _ in range(number_of_lines):
    words.update(input().split())
print(len(words))
