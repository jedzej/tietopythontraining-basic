def power(base, index):
    return base**index


correctInPut = None
while correctInPut is None:
    try:
        print(power(float(input()), int(input())))
        correctInPut = 1
    except ValueError:
        print('The first number must be real and the second integer')

