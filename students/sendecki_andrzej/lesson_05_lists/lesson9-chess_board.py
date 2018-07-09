#Given two numbers n and m. Create a two-dimensional array of size (n x m) and populate it with the characters "." and "*" in a checkerboard pattern. The top left corner should have the character "." .

def start_with_period(list):
    if j%2 == 0:
        list.append(".")
    else:
        list.append("*")

    return list
    
def start_with_star(list):
    if j%2 == 0:
        list.append("*")
    else:
        list.append(".")

    return list

print("Enter input list dimensions:")
n, m = [int(i) for i in raw_input().split()]

chessboard = []
row = []

for i in range(n):
    for j in range(m):
        if i%2 == 0:
            start_with_period(row)
        else:
            start_with_star(row)        
    chessboard.append(row)
    row = []

#print the chessboard
for i in range(n):
    for j in range(m):
        if j == m-1:
            print(chessboard[i][j])
        else:
            print(chessboard[i][j], end=" ")
