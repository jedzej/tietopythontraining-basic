def power(a, n):
	if n == 0:
		return 1
	else:
		return a ** n


print(power(float(input('Enter base of exponentiation: ')), int(input(
						'Enter exponent of exponentiation: '))))
