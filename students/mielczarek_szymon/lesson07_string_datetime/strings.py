# The number of words
print(input().count(' ') + 1)

# To swap the two words
words = input().split()
words[0], words[1] = words[1], words[0]
print(' '.join(words))

# Replace the substring
print(input().replace('1', 'one'))
