def main():
    dolarsPerCupcake = int(input())
    centsPerCupcake = int(input())
    quantity = int(input())
    totalDolars = quantity * dolarsPerCupcake + (centsPerCupcake * quantity) // 100
    totalCents = (centsPerCupcake * quantity) % 100
    print("{0} {1}".format(totalDolars, totalCents))

if __name__ == '__main__':
    main()
