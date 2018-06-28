'''
6. Args sum - write a function called sum_all that takes
 any number of arguments and returns their sum.
'''


def sum_all(*args):
    if len(args) > 0:
        sum = args[0]
        for i in range(1, len(args)):
            sum += args[i]
        return sum


if __name__ == "__main__":
    data = input("Enter numbers separated by space: ").split()
    list0 = [int(s) for s in data]
    list1 = [float(s) for s in data]
    list2 = data
    print(sum_all(*list0))
    print(sum_all(*list1))
    print(sum_all(*list2))
