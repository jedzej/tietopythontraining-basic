#!/usr/bin/env python3


def main():
    key_words = ["ADJECTIVE", "NOUN", "ADVERB", "VERB"]

    original_file = open("mad_libs_text.txt", "r")
    output_file = open("mad_libs_output.txt", "w")

    for line in original_file:
        for word in line.split(" "):
            if word in key_words:
                print("Enter " + word.lower() + ": ")
                replacement = str(input())
                output_file.write(replacement)
            else:
                output_file.write(word)
            output_file.write(" ")


if __name__ == "__main__":
    main()
