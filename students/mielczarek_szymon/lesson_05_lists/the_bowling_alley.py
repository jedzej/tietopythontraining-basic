num_of_pins, num_of_balls = [int(i) for i in input().split()]
result = ['I'] * num_of_pins
for i in range(num_of_balls):
    start_pos, stop_pos = [int(i) for i in input().split()]
    hit = ['.'] * (stop_pos - start_pos + 1)
    result[start_pos - 1: stop_pos] = hit

print(''.join(result))
