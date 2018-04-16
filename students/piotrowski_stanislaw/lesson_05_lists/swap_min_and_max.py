# piotrsta
# Swap min and max
# https://snakify.org/lessons/lists/problems/swap_min_and_max/

spam = [3, 4, 5, 2, 1]

min_value = min(spam)
max_value = max(spam)

min_index = spam.index(min_value)
max_index = spam.index(max_value)

spam[min_index], spam[max_index] = spam[max_index], spam[min_index]
for i in spam:
    print(i, end=' ')
