
def negative_exponent(num, exp):

    print(str(num ** exp).rstrip('0').rstrip('.'))


while True:
    try:
        print("Please enter a real number")
        number = float(input())
        print("Please enter the exponent")
        exponent = int(input())
        break
    except:
        print("Please enter a real number first, followed by an integer")

negative_exponent(number, exponent)
