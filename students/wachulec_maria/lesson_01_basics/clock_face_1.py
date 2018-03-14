H = int(input("Hours (H): "))
M = int(input("Minutes (M): "))
S = int(input("Seconds (S): "))

degree_seconds = S * 30
degree_minutes = M * 30 + (degree_seconds/60)
degree_hours = H * 30 + (degree_minutes/60)

print(degree_hours)
