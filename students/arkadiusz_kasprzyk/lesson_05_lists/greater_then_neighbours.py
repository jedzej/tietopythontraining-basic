def gtn(ll):
    s = 0
    if len(ll) >= 3:
        for k in range(1, len(ll) - 1):
            if ll[k] > ll[k - 1] and ll[k] > ll[k + 1]:
                s += 1
    return s

## ll = [1, 4, 6, 3, 8, 6, 9, 0, 3, 5, 4, 6, 7, 4]
## gtn(ll)

