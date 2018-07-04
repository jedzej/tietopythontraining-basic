def get_input():
    merged_str = ""
    while True:
        user_input = input()
        merged_str += str(user_input)
        if user_input == "0":
            break
    return merged_str


if __name__ == '__main__':
    chain = get_input()
    for i in reversed(chain):
        print(i)
