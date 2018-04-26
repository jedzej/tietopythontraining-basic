N, K = list(int(x) for x in input().split())

list_p = []
for x in range(K):
    points = list(int(x) for x in input().split())
    list_p.append(points)

res = list("I" * N)
for x in range(len(list_p)):
    start_p, stop_p = list_p[x]
    for p in range(start_p - 1, stop_p):
        res[p] = "."
