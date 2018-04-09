ll = [1, 4, 6, 3, 8, 6, 9, 0, 3, 5, 4, 6, 7, 4]

def greater_then_neighbours(ll):
    s = 0
    for k in range(1, len(ll)-1):
        if ll[k] > ll[k-1] and ll[k] > ll[k+1]:
            s += 1
    return s

print(greater_then_neighbours(ll))