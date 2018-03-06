# prints fractional part of a number
# caveat: "rounded" to 9 digits after comma
# otherwise it prints number not conformant to requested results

n = float(input())

print(round(n % 1, 10))
