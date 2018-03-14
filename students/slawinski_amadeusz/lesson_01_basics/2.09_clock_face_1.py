# give hour (h)m minutes (m) and seconds (s)
# print angle of the hour hand on clock
hour = int(input())
minutes = int(input())
seconds = int(input())

print (30 * hour + minutes / 2 + seconds/120)
