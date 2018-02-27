
import math
N = int(input())
M = int(input())
w1 = M // N
w2 = (M - N*w1)/M
print(w1 + math.ceil(w2))