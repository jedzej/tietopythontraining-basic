
def print_cost_of_cupcake():

    a = int(input("Provide cost of cupcake in dollars "))
    b = int(input("Provide cost of cupcake in cents "))
    n = int(input("Provide number of cupcakes "))

    cupcake_cost = n * (100 * a + b)
    print(cupcake_cost // 100, cupcake_cost % 100)


print_cost_of_cupcake()
