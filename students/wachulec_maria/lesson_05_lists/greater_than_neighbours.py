def greater_neighbours():
    sample_list = input().split()
    result = 0
    for i in range(len(sample_list) - 2):
        if sample_list[i + 1] > sample_list[i] and sample_list[i + 1] >\
                sample_list[i + 2]:
            result += 1
    print(result)
