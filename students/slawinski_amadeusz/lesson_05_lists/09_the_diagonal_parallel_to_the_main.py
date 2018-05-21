#!/usr/bin/env python3

dim = int(input())

matrix = [[str(abs(i - j)) for i in range(dim)] for j in range(dim)]

for i in range(dim):
    print(' '.join(matrix[i]))
