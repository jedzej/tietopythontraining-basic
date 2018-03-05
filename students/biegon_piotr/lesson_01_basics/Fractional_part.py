print("Fractional part\n")

a = float(input("Enter a float number: "))
real_a, frac_a = str(a).split(".")

if frac_a == "0":
    print("\nFractional part is 0")
else:
    print("\nFractional part is 0." + str(frac_a))