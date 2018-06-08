import os

if __name__ == '__main__':
    input_file_path = input('Enter text file path: ')

    if not os.path.exists(input_file_path):
        raise ValueError('Invalid text file path')

    if not os.path.isfile(input_file_path):
        raise ValueError('Given path is not a file')

    replacement_dict = {
        'ADJECTIVE': input('Enter adjective: '),
        'NOUN': input('Enter noun: '),
        'ADVERB': input('Enter adverb: '),
        'VERB': input('Enter verb: ')}

    output_file_path = input_file_path + '.new'

    with open(input_file_path, mode='r') as input_file:
        text = input_file.read()
        for k, v in replacement_dict.items():
            text = text.replace(k, v)

        print('\n' + text)

        with open(output_file_path, mode='x') as output_file:
            output_file.write(text)
