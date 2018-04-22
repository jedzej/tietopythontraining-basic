pins_and_balls = input().split()
balls = []
pins = ['I'] * int(pins_and_balls[0])

for i in range(int(pins_and_balls[1])):
    balls.append(input().split())
    for pin in range(int(balls[i][0]) - 1, int(balls[i][1])):
        pins[pin] = '.'

print(''.join(pins))
