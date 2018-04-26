n = int(input())


def generate_numbers(start_value, l):
    cnt_up = True if start_value == 0 else False
    r_list = []
    for x in range(l):
        if cnt_up:
            r_list.append(start_value)
            start_value += 1
        else:
            r_list.append(start_value)
            start_value -= 1
            if start_value == 0:
                cnt_up = True
    return r_list


def create_matrix(n):
    for x in range(n):
        row = generate_numbers(x, n)
        for v in row:
            print(v, end=' ')
        print()


create_matrix(n)
