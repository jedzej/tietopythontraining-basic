def bowling():
    num_of_pins = int(input('Give the number of pins: '))
    num_of_balls = int(input('Give the number of balls: '))
    score = ['I'] * num_of_pins
    for i in range(num_of_balls):
        knocked_start = int(input('Give the fist knocked position: '))
        knocked_end = int(input('Give the last knocked position: '))
        if knocked_start < 0 or knocked_end > num_of_pins:
            print('Incorrect value!')
            break
        for j in range(knocked_start-1, knocked_end):
            score[j] = '.'
    return score


result = bowling()
print(str(result))
