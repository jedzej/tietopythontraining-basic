def how_many_bricks(set):
    print(len(set))
    print(*[str(item) for item in sorted(set)])

N, M = [int(element) for element in input("How many cubes they have?").split()]
firstColor, secondColor = set(), set()

for i in range(N):
    firstColor.add(int(input("Give me a numerical color value for each cube in Alice\'s set")))

for x in range(M):
    secondColor.add(int(input("Give me a numerical color value for each cube in Bob\'s set")))

how_many_bricks(firstColor & secondColor)
how_many_bricks(firstColor - secondColor)
how_many_bricks(secondColor - firstColor)
