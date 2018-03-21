ah = 360/12
am = ah*1.0/60
ase = am/60

H = int (input("houer: "))
M = int (input("minut: "))
S = int (input("secund: "))
angle = ah *H + am *M + ase *S
print(angle)
