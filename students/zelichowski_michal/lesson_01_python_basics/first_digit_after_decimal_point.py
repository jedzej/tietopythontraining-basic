# Given a positive real number, print its first digit to the right of the decimal point.

a = float(input())
print(int(a * 10) % 10)
