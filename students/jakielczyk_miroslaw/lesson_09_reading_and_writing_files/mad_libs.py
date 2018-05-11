file = open('file_to_be_modified.txt', 'r')
source_text = file.read()
print(len(source_text))
file.close()

continue_search = True
while continue_search:
    continue_search = False
    if source_text.find('ADJECTIVE') != -1:
        continue_search = True
        print('Enter ADJECTIVE:')
        source_text = source_text.replace('ADJECTIVE', input(), 1)

    if source_text.find('VERB') != -1:
        continue_search = True
        print('Enter VERB:')
        source_text = source_text.replace('VERB', input(), 1)

    if source_text.find('ADVERB') != -1:
        continue_search = True
        print('Enter ADVERB:')
        source_text = source_text.replace('ADVERB', input(), 1)

    if source_text.find('NOUN') != -1:
        continue_search = True
        print('Enter NOUN:')
        source_text = source_text.replace('NOUN', input(), 1)

file = open('file_after_modification.txt', 'w')
target_text = source_text

file.write(target_text)

file.close()
