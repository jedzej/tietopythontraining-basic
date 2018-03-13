def main():
 startRow = int(input())
 startColumn = int(input())
 endRow = int(input())
 endColumn = int(input())
 rowDiff = abs(startRow - endRow)
 columnDiff = abs(startColumn - endColumn)

 if (rowDiff == 1 and columnDiff == 2) or (rowDiff == 2 and columnDiff == 1):
     print("YES")
 else:
     print("NO")

if __name__ == '__main__':
    main()
