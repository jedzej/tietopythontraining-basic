ll = [1, 4, 6, 3, 8, 6, 9, 0, 3, 5, 4, 6, 7, 4]

def swap_min_max(ll):
    lmin = min(ll)
    lmax = max(ll)
    imin = ll.index(lmin)
    imax = ll.index(lmax)
    ll[imin] = lmax
    ll[imax] = lmin
    return ll

print(swap_min_max(ll))
