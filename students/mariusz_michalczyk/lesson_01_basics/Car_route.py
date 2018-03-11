from math import ceil
kmperday = float(input("Enter km per day: "))
kmroute = float(input("Enter route km: "))

print ("It will take: " + str(ceil(kmroute / kmperday)))