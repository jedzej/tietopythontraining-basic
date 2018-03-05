print("Enter hours")
h = int(input())

print("Enter minutes")
m = int(input())

print("Enter seconds")
s = int(input())

h_angle = (360/12) * H
m_angle = (360/12)/60 * M
s_angle = ((360/12)/60)/60 * S

total_angle = h_angle + m_angle + s_angle

print("Angle: " + str(total_angle))
