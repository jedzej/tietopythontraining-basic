num = float(input("Enter positive real number\n"))
fr = (num - num // 1)
fr = fr * 10
fr = fr % 10
print('The first digit to the right of the decimal point is ' + str(int(fr)))
