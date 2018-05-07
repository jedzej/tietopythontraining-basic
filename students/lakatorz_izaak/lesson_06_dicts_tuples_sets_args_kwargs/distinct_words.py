

def main():
    text_lines = int(input('Enter number of lines: '))
    distinct_set = set()
    for line in range(text_lines):
        set_line = set(input().split(' '))
        distinct_set |= set_line
    print(len(distinct_set))


if __name__ == "__main__":
    main()
