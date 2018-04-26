m, n = list(int(x) for x in input().split())

list_p = []
for x in range(m):
    points = list(int(p) for p in input().split())
    list_p.append(points)


def maximum(list_f):
    max_value = max(max(list_f))
    # locate max value
    for x in range(m):
        for z in range(n):
            if list_f[x][z] == max_value:
                print(str(x) + " " + str(z))
                return


maximum(list_p)
