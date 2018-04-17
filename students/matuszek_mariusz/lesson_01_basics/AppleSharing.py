n = int(input('Number of students: '))
k = int(input('Number of apples: '))

print('Every student will get ' + str(k//n) + ' apples.')
print('Still will remain ' + str(k%n) + ' apples.')