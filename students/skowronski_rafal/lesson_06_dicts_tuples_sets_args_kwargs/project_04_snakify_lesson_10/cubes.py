def print_set(set):
    print(len(set))
    for element in sorted(set):
        print(element)


if __name__ == '__main__':
    alice_count, bob_count = \
        tuple([int(i) for i in input('Enter two integers separated by space: ')
              .split()])
    print('Enter Alice\'s set:')
    alice_set = set([int(input()) for i in range(alice_count)])
    print('Enter Bob\'s set:')
    bob_set = set([int(input()) for i in range(bob_count)])

    print('Answer: ')
    print_set(alice_set.intersection(bob_set))
    print_set(alice_set - bob_set)
    print_set(bob_set - alice_set)
