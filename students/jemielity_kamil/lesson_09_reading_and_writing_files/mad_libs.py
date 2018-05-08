mad_libs_file = open('mad_libs')
mad_libs_content = mad_libs_file.read()
mad_libs_file.close()

dictionary = {'ADJECTIVE': input('Enter an adjective: '),
              'NOUN': input('Enter a noun: '),
              'ADVERB': input('Enter an adverb: '),
              'VERB': input('Enter a verb: ')
              }

for i in dictionary:
    mad_libs_content = mad_libs_content.replace(i, dictionary[i])

print(mad_libs_content)

file = open('mad_libs_result', 'w')
file.write(mad_libs_content)
file.close()
