def fizzbuzz (n):
    if N % 3 == 0:
        return 'FIZZ'
    elif N % 5 == 0:
        return 'BUZZ'
    elif N % 3 == 0 and N % 5 == 0:
    else:
        return str(n)
    print
    "\n".join(fizzbuzz(n) for n in xrange(1, 21))





if __name__ == '__main__':
    fizzbuzz()