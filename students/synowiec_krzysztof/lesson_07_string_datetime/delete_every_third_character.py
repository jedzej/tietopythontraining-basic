def main():
    string = input()
    final_string = ""
    for x in range(len(string)):
        if x % 3 != 0:
            final_string += string[x]
    print(final_string)


if __name__ == '__main__':
    main()
