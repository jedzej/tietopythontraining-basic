print("Clock face - 1\n")

H = int(input("Enter the number of hours: "))
M = int(input("Enter the number of minutes: "))
S = int(input("Enter the number of seconds: "))

angle = float(H * (360/12)) + float(M * (360/(60*12))) + float(S * (360/(60*60*12)))

print("\nAngle is ", str(angle))