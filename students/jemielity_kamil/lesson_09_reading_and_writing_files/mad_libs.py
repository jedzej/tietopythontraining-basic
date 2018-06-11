with open('mad_libs') as mad_libs_file:
    mad_libs_content = mad_libs_file.read()


dictionary = {'ADJECTIVE': input('Enter an adjective: '),
              'NOUN': input('Enter a noun: '),
              'ADVERB': input('Enter an adverb: '),
              'VERB': input('Enter a verb: ')
              }

for old_word, new_word in dictionary.items():
    mad_libs_content = mad_libs_content.replace(old_word, new_word)

print(mad_libs_content)

file = open('mad_libs_result', 'w')
file.write(mad_libs_content)
file.close()
