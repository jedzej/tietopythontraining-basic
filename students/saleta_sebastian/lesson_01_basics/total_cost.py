def get_total_costs():
    dollars = int(input())
    cents = int(input())
    num_of_cupcakes = int(input())
    cost = num_of_cupcakes * (100 * dollars + cents)
    cost_in_dollars = (cost // 100)
    cost_in_cents = (cost % 100)

    print('Total cost in dollar is {} and total cost in cents is {}'.format(cost_in_dollars, cost_in_cents))

if __name__ == '__main__':
    get_total_costs()