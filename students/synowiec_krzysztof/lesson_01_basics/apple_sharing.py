
def main():
    numberOfStudents = int(input())
    numberOfApples = int(input())
    
    applesPerStudent = numberOfApples // numberOfStudents
    applesRemain = numberOfApples % numberOfStudents
    print(applesPerStudent)
    print(applesRemain)

if __name__ == '__main__':
    main()
