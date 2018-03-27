def ladder():
    steps_count = int(input())
    ladder = ""
    for i in range(steps_count):
        ladder += str(i+1)
        print(ladder)


if __name__ == '__main__':
    ladder()