class CollatzSequence(object):

    def collatz(self, number):
        if number % 2 == 0:
            print(number // 2)
            return number // 2
        elif number % 2 == 1:
            print(3 * number + 1)
            return 3 * number + 1

    def pick_number(self, number):
        result = self.collatz(number)
        while result != 1:
            number = self.collatz(result)
            result = self.collatz(number)

    def __init__(self):
        try:
            number = int(input('Enter number: '))
            self.pick_number(number)
        except ValueError:
            print('Only integers accepted')


c = CollatzSequence()
