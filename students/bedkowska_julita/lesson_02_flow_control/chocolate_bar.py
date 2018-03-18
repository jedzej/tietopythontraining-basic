barLength = int(input('Give the bar length: '))
barHeight = int(input('Give the bar height: '))
piece = int(input('Give the number of pieces: '))

result = 'NO'
if (piece % barLength == 0 or piece % barHeight == 0) and \
        piece < barHeight * barLength:
    result = 'YES'

print('{} {}'.format('Is split possible:', result))
