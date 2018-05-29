# Function called inspect_args that prints passed args
# and kwargs in human-readable format.


def inspect_args(*args, **kwargs):
    print('Arguments:', ', '.join(map(str, args)))
    print('Keyword :')
    for k, v in kwargs.items():
        print(k, "=", v)


my_dict = {'o': '8', 'p': 9}
inspect_args(5, 7, 8, **my_dict, n=9)
print()
inspect_args(5, 7, 8, n=9, **my_dict)
