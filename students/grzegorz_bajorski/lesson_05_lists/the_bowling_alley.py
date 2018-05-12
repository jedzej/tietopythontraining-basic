pins_val, balls_val = [int(i) for i in input().split()]

pins = ['I'] * pins_val

for _ in range(balls_val):
        start, stop = [int(i) for i in input().split()]
        for pin in range(start - 1, stop):
            pins[pin] = '.'

print(''.join(pins))
