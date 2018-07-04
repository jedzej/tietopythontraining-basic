"""
Program use "set", print results for:
intersection (A & B)
relative complement of B in A (A - B)
relative complement of A in B (B - A)

Inputs:
n - number of Alice's cubes
m - number of Bob's cubes
n cubes colors (for Alice)
m cubes colors (for Bob)

Output:
Number of cubes repeated with Alice and Bob
Cubes colors repeated with Alice and Bob
Number of Alice cubes not repeated (Bob doesn't have the same colors)
Alice cubes colors not repeated (Bob doesn't have the same colors)
Number of Bob cubes not repeated (Alice doesn't have the same colors)
Bob cubes colors not repeated (Alice doesn't have the same colors)
"""
from functions_lesson06 import list_random


n = int((input("Number of Alice's cubes: ")))
print("Alce's cubes:")
# alice_cubes = list_random(n, 0, 10)
alice_cubes = list_random(n, 0, 10**8)
m = int((input("Number of Bob's cubes: ")))
print("Bob's cubes:")
# bob_cubes = list_random(m, 0, 10)
bob_cubes = list_random(m, 0, 10**8)

# Number of cubes repeated with Alice and Bob
# Cubes colors repeated with Alice and Bob
repeated_cubes = list(set(alice_cubes) & set(bob_cubes))
print("Number repeated cubes colors: ", len(repeated_cubes))
print("Repeated cubes:")
print(' '.join(map(str, repeated_cubes)))

# Number of Alice cubes not repeated (Bob hasn't the same colors)
# Alice cubes colors not repeated (Bob hasn't the same colors)
alice_cubes_unique = list(set(alice_cubes) - set(bob_cubes))
print("Number of Alice cubes not repeated: ", len(alice_cubes_unique))
print("Alice cubes colors not repeated:")
print(' '.join(map(str, alice_cubes_unique)))

# Number of Bob cubes not repeated (Alice hasn't the same colors)
# Bob cubes colors not repeated (Alice hasn't the same colors)
bob_cubes_unique = list(set(bob_cubes) - set(alice_cubes))
print("Number of Bob cubes not repeated: ", len(bob_cubes_unique))
print("Bob cubes colors not repeated:")
print(' '.join(map(str, bob_cubes_unique)))
