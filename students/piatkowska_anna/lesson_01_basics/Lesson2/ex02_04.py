#Statement
#Given a positive real number, print its fractional part.
print("Please enter positive real number:")
a = float(input())
a = a-int(a)
print("Fractional part: " + str(round(a,3)))