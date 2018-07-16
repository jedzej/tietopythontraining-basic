def guess_the_number():
    max = int(input("Enter maximum secret number:"))
    secret_set = set(range(1, max + 1))
    print("Enter Beatrice guess set of number separated by space")
    beatrice_set = {int(s) for s in input().split()}
    print("Enter Augustus answear (YES/NO):")
    augustus_answear = str(input())
    while(beatrice_set != 'HELP'):
        if(augustus_answear == 'NO'):
            secret_set = secret_set - set(beatrice_set)
        else:
            secret_set = secret_set & set(beatrice_set)
        beatrice_set = input("Enter Beatrice guess set of number \
separated by space or HELP to end: ")
        if beatrice_set != 'HELP':
            beatrice_set = [int(s) for s in beatrice_set.split()]
            augustus_answear = str(input("Enter Augustus answear (YES/NO):"))
    secret_set = list(secret_set)
    secret_set.sort()
    print("Secret number set:")
    for i in range(len(secret_set)):
        print(secret_set[i], end=" ")

if __name__ == "__main__":
    guess_the_number()