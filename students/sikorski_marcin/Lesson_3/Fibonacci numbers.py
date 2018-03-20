def fib(x):
    if x <= 1:
        return x
    else:
        return fib(x-1)+ fib(x-2)

which_number_user_wants_to_calculate = float(input("Which Fibonnaci number you want to see? "))

print(fib(which_number_user_wants_to_calculate))