def power(base, index):
    if index == 0:
        return 1
    else:
        return base * power(base, index - 1)


correctInPut = None
while correctInPut is None:
    try:
        print(power(float(input()), int(input())))
        correctInPut = 1
    except ValueError:
        print('The first number must be real and the second integer')
