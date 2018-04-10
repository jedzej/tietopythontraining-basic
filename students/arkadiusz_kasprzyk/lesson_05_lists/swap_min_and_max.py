def swap_min_max(ll):
    if len(ll) >= 2:
        lmin, lmax = min(ll), max(ll)
        imin, imax = ll.index(lmin), ll.index(lmax)
        ll[imin], ll[imax]= lmax, lmin
    return ll

#ll = [3, 0, 1, 4, 7, 2, 6]
#print(swap_min_max(ll))

