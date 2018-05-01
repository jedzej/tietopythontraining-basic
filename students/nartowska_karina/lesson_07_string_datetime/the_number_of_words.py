def number_of_words(text):
    print(text.count(" ") + 1)


def main():
    print("Enter text:")
    text = input()
    print("Result:")
    number_of_words(text)


if __name__ == "__main__":
    main()
