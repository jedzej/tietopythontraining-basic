def get_input():
    merged_str = ""
    while True:
        i = input()
        merged_str += str(i)
        if i == "0":
            break
    return merged_str


def reverse(str):
    return str[::-1]


if __name__ == '__main__':
    chain = get_input()
    print(reverse(chain))
