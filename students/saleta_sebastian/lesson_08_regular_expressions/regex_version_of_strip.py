import re


def alternative_strip(word, character):
    if not character:
        word_regex = re.compile(r'\s+')
        return word_regex.sub('', word)
    else:
        word_regex = re.compile(r'^[{}]+|[{}]+$'.format(character, character))
        return word_regex.sub('', word)


def main():
    print(alternative_strip('sssSebastianssssss', 's'))
    print(alternative_strip('    Saleta    Sebastian    ', None))


if __name__ == '__main__':
    main()
