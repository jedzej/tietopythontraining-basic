ah = 360 / 12
am = ah * 1.0 / 60
ase = am / 60

h = int(input("houer: "))
m = int(input("minut: "))
s = int(input("secund: "))
angle = ah * h + am * m + ase * s
print(angle)
