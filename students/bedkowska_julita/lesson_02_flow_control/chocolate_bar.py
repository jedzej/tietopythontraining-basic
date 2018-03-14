barLength = int(input())
barHeight = int(input())
piece = int(input())

result = 'NO'
if ((piece % barLength == 0) or (piece % barHeight == 0)) and piece < barHeight*barLength:
    result = 'YES'

print("Is split possible: "+result)
