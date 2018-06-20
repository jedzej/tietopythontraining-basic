def greater_than_neighbours():
    int_list = input("Enter a list of integer numbers separate by space: ")
    new_list = int_list.split()
    quanity = 0
    if len(new_list) >= 3:
        for i in range(1, len(new_list) - 1):
            if new_list[i] > new_list[i + 1]:
                quanity += 1
    print("Numbers of elements greater than neighbours: ", quanity)


def swap_min_and_max():
    a = [int(s) for s in input("Give a list of unique integer  numbers seperate by space: ").split()]
    index_of_min = 0
    index_of_max = 0
    for i in range(1, len(a)):
        if a[i] > a[index_of_max]:
            index_of_max = i
        if a[i] < a[index_of_min]:
            index_of_min = i
    a[index_of_min], a[index_of_max] = a[index_of_max], a[index_of_min]
    print("Result of swap the minimal and maximal elements of the list: ", ' '.join([str(i) for i in a]))


def the_bowling_alley():
    n, k = [int(s) for s in input("Enter number of pins and number of balls: ").split()]
    bahn = ['I'] * n
    for i in range(k):
        left, right = [int(s) for s in input().split()]
        for j in range(left - 1, right):
            bahn[j] = '.'
    print("Result: ", ''.join(bahn))


def maximum():
    n, m = [int(i) for i in input("Enter number for row and column seperate by space: ").split()]
    a = [[int(j) for j in input("").split()] for i in range(n)]
    best_i, best_j = 0, 0
    curr_max = a[0][0]
    for i in range(n):
        for j in range(m):
            if a[i][j] > curr_max:
                curr_max = a[i][j]
                best_i, best_j = i, j
    print("Result: ", best_i, best_j)


def chess_board():
    n, m = [int(i) for i in input("Enter two integer numbers with space between: ").split()]
    a = []
    for i in range(n):
        a.append([])
        for j in range(m):
            if (i + j) % 2 == 0:
                a[i].append('.')
            else:
                a[i].append('*')
    for row in a:
        print(' '.join(row))


def swap_the_columns():
    def swap_columns(a, i, j):
        for k in range(len(a)):
            a[k][i], a[k][j] = a[k][j], a[k][i]

    n, m = [int(i) for i in input("Enter rows and columns numbers: ").split()]
    a = [[int(j) for j in input("Enter numbers: ").split()] for i in range(n)]
    i, j = [int(i) for i in input("Swap column: ").split()]
    swap_columns(a, i, j)
    print('\n'.join([' '.join([str(i) for i in row]) for row in a]))


def age_calculator(ages):
    adults = [age for age in ages if age >= 18]
    children = [age for age in ages if age < 18]

    if len(adults) > 0:
        avg_adults = sum(adults) / len(adults)
    else:
        avg_adults = "No adults"
    print("The average age of adults is: ", avg_adults)
    print("Number of children: " + str(len(children)))


def main():
    # print(age_calculator(ages))
    swap_the_columns()


if __name__ == '__main__':
    # greater_than_neighbours()
    # swap_min_and_max()
    # the_bowling_alley()
    # maximum()
    #chess_board()
    #swap_the_columns()
    # ages = [int(i) for i in input("Enter list of people's ages ").split()]
    # age_calculator(ages)