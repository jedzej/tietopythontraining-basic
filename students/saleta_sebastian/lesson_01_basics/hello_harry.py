def hello(name):
    WELCOME = 'Hello'
    print(WELCOME + ', ' + name + '!')


if __name__ == '__main__':
    name = raw_input()
    hello(name)