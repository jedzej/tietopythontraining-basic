def comma_code(values):
    return ", ".join(x for x in values[:-1]) + ', and ' + values[-1]


def main():
    print("Enter a list value:")
    list_value = input()
    values = list_value.split()
    print(comma_code(values))


if __name__ == "__main__":
    main()
