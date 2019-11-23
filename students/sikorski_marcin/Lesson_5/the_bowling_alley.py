greeting_message = input(" Give me the number of pins N and then the number of balls K "
                                             "\nto be rolled, followed by K pairs of numbers (one for each "
                                             "\nball rolled), so I can determine which pins remain standing "
                                             "\nafter all the balls have been rolled. Finish by typying ENTER:"
                                             "\n")

pins, balls = [int(s) for s in greeting_message.split()]

all_pins = ['I'] * pins

for i in range(balls):
    left, right = [int(s) for s in input().split()]
    for j in range(left - 1, right):
        all_pins[j] = '.'

print(''.join(all_pins))
