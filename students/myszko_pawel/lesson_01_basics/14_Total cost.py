# A cupcake costs A dollars and B cents. Determine, how many dollars and cents should one pay for N cupcakes.
# A program gets three numbers: A, B, N. It should print two numbers: total cost in dollars and cents.

# Read an integer:
A = int(input())
B = int(input())
N = int(input())
# Print a value:
cup_cost_in_cents = A*100 + B
total_cost_in_cents = cup_cost_in_cents * N
cost_in_dol = total_cost_in_cents // 100
cost_in_cen = total_cost_in_cents % 100
print(cost_in_dol)
print(cost_in_cen)