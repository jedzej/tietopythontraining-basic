# piotrsta
# comma code
# https://automatetheboringstuff.com/chapter4/


def comma_code(input_list):
    output_string = ''
    for i in range(len(input_list)-1):
        output_string += str(input_list[i]) + ', '
    output_string += 'and ' + str(input_list[-1])
    return output_string


if __name__ == '__main__':
    spam = ['apples', 'bananas', 'tofu', 'cats']

    print(comma_code(spam))
