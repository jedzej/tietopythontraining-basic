file = open('file_to_be_modified.txt', 'r')
source_text = file.read()
file.close()

nearest_word_position = 0
starting_search_position = 0

adjective_position = 0
verb_position = 0
adverb_position = 0
noun_position = 0

word_to_be_replaced = ''
new_word = ''

while word_to_be_replaced is not None:
    word_to_be_replaced = None
    adjective_position = source_text.find('ADJECTIVE', starting_search_position)
    verb_position = source_text.find('VERB', starting_search_position)
    adverb_position = source_text.find('ADVERB', starting_search_position)
    noun_position = source_text.find('NOUN', starting_search_position)

    if adjective_position != -1:
        nearest_word_position = adjective_position
        word_to_be_replaced = 'ADJECTIVE'

    if verb_position != -1:
        if word_to_be_replaced is None or verb_position < nearest_word_position:
            nearest_word_position = verb_position
            word_to_be_replaced = 'VERB'

    if adverb_position != -1:
        if word_to_be_replaced is None or adverb_position < nearest_word_position:
            nearest_word_position = adverb_position
            word_to_be_replaced = 'ADVERB'

    if noun_position != -1:
        if word_to_be_replaced is None or noun_position < nearest_word_position:
            nearest_word_position = noun_position
            word_to_be_replaced = 'NOUN'

    if word_to_be_replaced is not None:
        print('Enter a', word_to_be_replaced.lower(), ':')
        new_word = input()
        source_text = source_text.replace(word_to_be_replaced, new_word, 1)

    starting_search_position += len(new_word)

file = open('file_after_modification.txt', 'w')
target_text = source_text
file.write(target_text)
file.close()
