def main():
 startRow = int(input())
 startColumn = int(input())
 endRow = int(input())
 endColumn = int(input())
 rowDiff = abs(startRow - endRow)
 columnDiff = abs(startColumn - endColumn)

 if rowDiff == columnDiff:
     print("YES")
 else:
     print("NO")

if __name__ == '__main__':
    main()
