def swap_two_words(text):
    text = text.split()
    print(text[1] + " " + text[0])


def main():
    print("Enter words:")
    text = input()
    print("Result:")
    swap_two_words(text)


if __name__ == "__main__":
    main()
