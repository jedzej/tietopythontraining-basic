print("First digit after decimal point\n")

a = float(input("Enter a float number: "))
real_a, frac_a = str(a).split(".")

print("\nFirst digit of fractional part is " + str(frac_a[0]))