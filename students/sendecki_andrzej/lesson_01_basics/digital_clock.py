# lesson_01_basics
# Digital clock
#
# Statement
# Given the integer N - the number of minutes that is passed since midnight -
# how many hours and minutes are displayed on the 24h digital clock?
# The program should print two numbers: the number of hours (between 0 and 23)
# and the number of minutes (between 0 and 59). 

print("Enter the number of minutes from midnight")
m = int(input())

res_h = (m // 60) % 24
res_m = m - (m // 60) * 60

print("It is " + str(res_h) + ":" + str(res_m))

