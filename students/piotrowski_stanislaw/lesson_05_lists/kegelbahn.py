# piotrsta
# The bowling alley (kegelbahn)
# https://snakify.org/lessons/lists/problems/kegelbahn/

n, k = 10, 3

pins = n * ['I']

# an example of input data
# start, stop = 8 10
# start, stop = 2 5
# start, stop = 3 6

for i in range(k):
    start, stop = [int(i) for i in input('Enter a pair of input data no.' + str(i + 1) + '(sep. by a space): ').split()]
    for pin in range(start-1, stop):
        pins[pin] = '.'

print(''.join(pins))
