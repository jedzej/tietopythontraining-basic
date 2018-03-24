def get_number_of_zeros():
    a = int(input())
    zeros = 0

    for i in range(1, a + 1):
        i = int(input())

        if i == 0:
            zeros += 1

    print(zeros)


if __name__ == '__main__':
    get_number_of_zeros()
