array_size = input()
pins = int((array_size.split(' '))[0])
balls = int((array_size.split(' '))[1])
pins_list = []
for pin in range(pins):
    pins_list.append('I')
for x in range(balls):
    pair = input().split(' ')
    pin_start = int(pair[0])
    pin_stop = int(pair[1])
    for y in range(pin_start-1, pin_stop):
        pins_list[y] = '.'
print(' '.join(pins_list))
