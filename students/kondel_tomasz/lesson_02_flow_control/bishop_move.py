x_1 = int(input())
y_1 = int(input())
x_2 = int(input())
y_2 = int(input())

# line function for 2 points: (x2−x1)(y−y1)=(y2−y1)(x−x1)
# additional points for function -/+45deg
x_1_plus_45 = x_1 + 1
y_1_plus_45 = y_1 + 1
x_1_minus_45 = x_1 + 1
y_1_minus_45 = y_1 - 1

result_plus = (x_2 - x_1) * (y_1_plus_45 - y_1) - (y_2 - y_1) * \
                                                  (x_1_plus_45 - x_1)
result_minus = (x_2 - x_1) * (y_1_minus_45 - y_1) - (y_2 - y_1) * \
                                                    (x_1_minus_45 - x_1)

if (result_plus == 0) or (result_minus == 0):
    print('YES')
else:
    print('NO')
