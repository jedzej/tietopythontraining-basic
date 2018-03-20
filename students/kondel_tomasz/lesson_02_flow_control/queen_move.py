x_1 = int(input())
y_1 = int(input())
x_2 = int(input())
y_2 = int(input())

# line function for 2 points: (x2−x1)(y−y1)=(y2−y1)(x−x1)
# additional points for function -/+45deg, 90deg, 0 deg
x_1_plus_45_deg = x_1 + 1
y_1_plus_45_deg = y_1 + 1
x_1_minus_45_deg = x_1 + 1
y_1_minus_45_deg = y_1 - 1
x_1_90_deg = x_1
y_1_90_deg = y_1 + 1
x_1_0_deg = x_1 + 1
y_1_0_deg = y_1

result_plus45 = (x_2 - x_1) * (y_1_plus_45_deg - y_1) - \
                (y_2 - y_1) * (x_1_plus_45_deg - x_1)
result_minus45 = (x_2 - x_1) * (y_1_minus_45_deg - y_1) - \
                 (y_2 - y_1) * (x_1_minus_45_deg - x_1)
result_90_deg = (x_2 - x_1) * (y_1_90_deg - y_1) - \
                (y_2 - y_1) * (x_1_90_deg - x_1)
result_0_deg = (x_2 - x_1) * (y_1_0_deg - y_1) - \
               (y_2 - y_1) * (x_1_0_deg - x_1)


if (result_plus45 == 0) or (result_minus45 == 0) or \
        (result_90_deg == 0) or (result_0_deg == 0):
    print('YES')
else:
    print('NO')
