# piotrsta
# Greater than neighbours
# https://snakify.org/lessons/lists/problems/greater_than_neighbours/

spam = [1, 5, 1, 5, 1]

counter = 0

for i in range(1, len(spam) - 1):
    if spam[i] > spam[i + 1] and spam[i] > spam[i - 1]:
        counter += 1
print(counter)
