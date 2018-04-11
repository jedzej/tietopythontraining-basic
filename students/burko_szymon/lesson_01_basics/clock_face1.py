h = int(input("Hours: "))
m = int(input("Minutes: "))
s = int(input("Seconds: "))

hour_a = 360/12
min_a = hour_a/60
sec_a = min_a/60


angle = (h * hour_a  +  m * min_a  + s * sec_a )
print( str(angle))