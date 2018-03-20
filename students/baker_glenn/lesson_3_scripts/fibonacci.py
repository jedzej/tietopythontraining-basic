def fib(number, last_num, next_num):
    if number > 1:
        number -= 1
        summed_numbers = next_num + last_num
        last_num = next_num
        fib(number, last_num, summed_numbers)
    else:
        print(next_num)


while True:
    try:
        print("Please enter a number")
        number = int(input())
        break
    except:
        print("Please enter a real number first, followed by an integer")
next_seq_number = 1
last_seq_number = 0
fib(number, last_seq_number, next_seq_number)
