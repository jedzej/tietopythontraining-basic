# Read a real number
a_str = input()
a_float = float(a_str)
a_int = int(a_float)
# Print its fractional part
print(round(a_float - a_int, len(a_str) - len(str(a_int)) - 1))
