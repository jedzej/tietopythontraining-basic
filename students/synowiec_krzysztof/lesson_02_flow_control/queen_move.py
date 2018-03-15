def main():
 startRow = int(input())
 startColumn = int(input())
 endRow = int(input())
 endColumn = int(input())
 rowDiff = abs(startRow - endRow)
 columnDiff = abs(startColumn - endColumn)

 diagonal = rowDiff == columnDiff
 horizontal = startRow == endRow
 vertical = startColumn == endColumn

 if diagonal or vertical or horizontal:
     print("YES")
 else:
     print("NO")

if __name__ == '__main__':
    main()

