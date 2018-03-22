# The program print two numbers:
# the number of hours and the number of minutes when read minutes

N = int(input("Put minutes: "))
H = (N // 60)
M = N - H * 60

print(N, "minute/s =", H, "hour/s and ", M, "minute/s.")
