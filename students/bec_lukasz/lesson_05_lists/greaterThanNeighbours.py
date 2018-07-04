class GreaterThanNeighbours:

    def compose_list():

        my_list = []

        while True:
            element = input('Wpisz numer: ')
            if element == '':
                break
            my_list = my_list + [element]

        return my_list

    def monitor_neighbours(list):

        greatest_neighbours = []

        if len(list) >= 3:
            for i in range(len(list)):
                if 0 < i < len(list) - 1:
                    previous = list[i - 1]
                    current = list[i]
                    next = list[i + 1]

                    if previous < current > next:
                        greatest_neighbours += [current]

        return greatest_neighbours

    if __name__ == '__main__':
        print(monitor_neighbours(compose_list()))
