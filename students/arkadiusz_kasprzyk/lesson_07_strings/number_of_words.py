# number_of_words.py


def words_number(string):
    nr = string.count(" ") + 1
    return nr


if __name__ == "__main__":
    nr = words_number(input("Give a string: "))
    print("Number of words is: ", nr)
