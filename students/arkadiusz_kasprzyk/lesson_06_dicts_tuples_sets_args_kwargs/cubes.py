# cubes.py


def cubes(aset, bset):
    sets_sum = aset | bset
    aset_only = aset - bset
    bset_only = bset - aset
    return sets_sum, aset_only, bset_only


def into_set(n=0, aset=set()):
    """
    Examples
    --------
    into_set()
    into_set(2)
    """
    print("Enter elements of the set (only integers!): ")
    for k in range(n):
        aset |= {int(input("{}: ".format(k + 1)))}
    print(aset)
    return aset


def print_set(aset):
    print("{} elements in the set".format(len(aset)))
    for e in aset:
        print(e)


if __name__ == "__main__":

    nums = []
    while len(nums) < 2:
        nums += input("Give numbers of elements in sets: ").split(" ")

    nums = nums[:2]
    nums = [int(n) for n in nums]

    for s in cubes(into_set(nums[0], set()), into_set(nums[1], set())):
        print_set(s)
