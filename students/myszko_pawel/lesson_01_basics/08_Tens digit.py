# Given an integer. Print its tens digit.


a = int(input())
if a < 10:
    print('0')
else:
    a = str(a)
    # Print a value:
    print(a[-2])
