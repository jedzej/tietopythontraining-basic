# clock face -1
#by tk

#podanie danych
hour  = int(input())
min = int(input())
sec = int(input())

h_to_angle = (30 * hour )
m_to_angle = (30 * min / 60)
s_to_angle = (30 * sec  / 3600)

angle = h_to_angle+m_to_angle+s_to_angle
print (angle)

