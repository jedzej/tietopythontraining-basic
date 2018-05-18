# Given an integer n, produce a two-dimensional array of size (n×n)
# and complete it according to the following rules, and print with
# a single space between characters:
# On the main diagonal write 0 .
# On the diagonals adjacent to the main, write 1 .
# On the next adjacent diagonals write 2 and so forth.
# Print the elements of the resulting array

def main():
    n = int(input())
    array = []

# creating array and 
    for row in range(n):
        array.append([0] * n)

    for row in range(n):
        for col in range(n):
            array[row][col] = abs(col -row)

# printing result
    for row in array:
        print(' '.join([str(elem) for elem in row]))

if __name__ == "__main__":
    main()
