# cubes.py


def cubes(aset, bset):
    sets_inter = aset & bset
    aset_only = aset - bset
    bset_only = bset - aset
    return sets_inter, aset_only, bset_only


def read_list(message="Enter elements: ", n=1):
    print(message)
    lst = []
    for k in range(n):
        lst.append(input("{}: ".format(k + 1)))
    return lst


def print_set(aset):
    print("{} elements in the set".format(len(aset)))
    ll = list(aset)
    ll.sort()
    for e in ll:
        print(e)


if __name__ == "__main__":

    nums = []
    while len(nums) < 2:
        nums += input("Give numbers of elements in sets: ").split()

    nums = list(map(int, nums[:2]))

    sets = tuple(map(lambda n: set(map(int, read_list(n=n))), nums))
    for s in cubes(*sets):
        print_set(s)
