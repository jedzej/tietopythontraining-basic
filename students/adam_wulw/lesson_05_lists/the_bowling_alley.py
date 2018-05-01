input_str = input()
N, K = input_str.split()
pins_state = ['I'] * int(N)
for i in range(int(K)):
    data = input()
    n, k = data.split()
    for j in range(int(n) - 1, int(k)):
        pins_state[j] = '.'
print(''.join(pins_state))
