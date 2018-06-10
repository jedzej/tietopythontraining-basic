def sum_all(*argv):
    sum_of_all = 0
    for arg in argv:
        sum_of_all += arg
    print(sum_of_all)


sum_all(1, 2, 3, 4, 5, 6)
