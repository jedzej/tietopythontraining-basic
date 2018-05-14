# def swap_min_and_max(numbers):
#     index_of_min_num = 0
#     index_of_max_num = 0
#
#     for i in range(1, len(numbers)-1):
#         print(numbers[i])
#         print(numbers[index_of_max_num])
#         if numbers[i] > numbers[index_of_max_num]:
#             index_of_max_num = numbers[i]
#         if numbers[i] < index_of_min_num:
#             index_of_min_num = numbers[i]
#
#     numbers[index_of_min_num], numbers[index_of_max_num] = numbers[index_of_max_num], numbers[index_of_min_num]
#     print(' '.join([str(i) for i in numbers]))
#     print([index_of_max_num], [index_of_min_num])

def swap_min_and_max(numbers):
    a = [int(s) for s in input().split()]
    index_of_min = 0
    index_of_max = 0
    for i in range(1, len(a)):
        if a[i] > a[index_of_max]:
            index_of_max = i
        if a[i] < a[index_of_min]:
            index_of_min = i
    a[index_of_min], a[index_of_max] = a[index_of_max], a[index_of_min]
    print(' '.join([str(i) for i in a]))


def main():
    #sample_list = [3, 4, 5, 2, 1]
    #answer = [3, 4, 1, 2, 5]
    sample_list = [int(i) for i in input().split()]
    swap_min_and_max(sample_list)


if __name__ == '__main__':
    main()
