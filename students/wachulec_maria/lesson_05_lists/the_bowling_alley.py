def bowling():
    pins_number, balls_numbers = input().split()
    score = ['I'] * int(pins_number)
    for i in range(int(balls_numbers)):
        start_pin, stop_pin = [int(s) for s in input().split()]
        start_pin -= 1
        score[start_pin:stop_pin] = '.' * (stop_pin - start_pin)
    return ''.join(score)


result = bowling()
print(result)
