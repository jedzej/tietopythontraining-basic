print("Enter hours")
h = int(input())

print("Enter minutes")
m = int(input())

print("Enter seconds")
s = int(input())

h_angle = (360/12) * h
m_angle = (360/12)/60 * m
s_angle = ((360/12)/60)/60 * s

total_angle = h_angle + m_angle + s_angle

print("Angle: " + str(total_angle))
