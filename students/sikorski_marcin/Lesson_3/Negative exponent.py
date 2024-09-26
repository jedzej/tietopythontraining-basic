def power(a,n):
    if n == 0:
        return 1
    else:
        return a**n

while True:
    real_number = int(input("Type real, positive number"))
    if real_number <= 0:
        print("I said POSITIVE")
        continue
    else:
        real_power = int(input("Now type power: "))
        print(power(real_number, real_power))
        break