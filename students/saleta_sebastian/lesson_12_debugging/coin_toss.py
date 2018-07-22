import random
import logging


logging.basicConfig(level=logging.DEBUG, format=(' %(asctime)s - %(levelname)'
                                                 's - %(message)s'))


COIN_SIDES = ('HEADS', 'TAILS')


def get_user_guess():
    usr_guess = ''
    while usr_guess not in COIN_SIDES:
        print('Guess the coin toss! Enter heads or tails:')
        usr_guess = input().upper()
        logging.debug('User choice: {}'.format(usr_guess))
    return usr_guess.upper()


def coin_toss_game():
    guess = get_user_guess()

    toss = COIN_SIDES[random.randint(0, 1)]  # 0 is tails, 1 is heads
    logging.debug('Toss is: {}'.format(toss))
    if toss == guess:
        logging.debug('User got it. Toss = {} and guess = {}'.format(toss,
                                                                     guess))
        print('You got it!')
    else:
        logging.debug('Guess fail. Gues = {} and Toss = {}'.format(guess,
                                                                   toss))
        print('Nope! Guess again!')
        guess = get_user_guess()
        if toss == guess:
            print('You got it!')
        else:
            logging.debug('Last guess was wrong. '
                          'Gues = {} and Toss = {}'.format(guess, toss))
            print('Nope. You are really bad at this game.')


def main():
    coin_toss_game()


if __name__ == '__main__':
    main()
