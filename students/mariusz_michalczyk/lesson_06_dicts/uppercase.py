def capitalize(lower_case_word):
    map = {}
    index = 0
    for char in lower_case_word:
        map[index] = char
        index += 1
    map[0] = map[0].upper()
    return "".join(map.values())


def capitalize_strs(strs):
    cap_strs = []
    for str in strs:
        cap_strs.append(capitalize(str))
    return cap_strs


if __name__ == '__main__':
    strs_array = [s for s in input().split()]
    print(" ".join(capitalize_strs(strs_array)))
