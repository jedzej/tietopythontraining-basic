# The Collatz Sequence

def collatz(number):
    if (number % 2) == 0:
        m = number // 2
        print(number, "\\", "2 =", m)
        return (m)
    else:
        m = 3 * number + 1
        print("3 *", number, "+ 1 =", m)
        return (m)

n = int((input("put number to check:")))

while (n != 1):
    n = collatz(n)
