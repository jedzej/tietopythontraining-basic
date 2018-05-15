def func():
    n = int(input())
    temp_dict = {}
    tuples_list = []

    for i in range(n):
        line = str(input()).split()
        for word in line:
            if word not in temp_dict:
                temp_dict.update({word: 1})
            else:
                temp_dict[word] += 1

    for k, v in temp_dict.items():
        tuples_list.append((v, k))

    tuples_list = sorted(tuples_list, reverse=True)
    for i in range(tuples_list[0][0], 0, -1):
        temp = []
        for j in tuples_list:
            if j[0] == i:
                temp.append(j)
        temp = sorted(temp)
        for x in temp:
            print(x[1])


def main():
    func()


if __name__ == '__main__':
    main()
