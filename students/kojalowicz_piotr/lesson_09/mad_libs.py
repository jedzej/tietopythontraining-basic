ml_file = open('mad_libs.txt')
ml_content = ml_file.read()
ml_file.close()


dictionary = {'ADJECTIVE': input('Enter an adjective: '),
              'NOUN': input('Enter a noun: '),
              'ADVERB': input('Enter an adverb: '),
              'VERB': input('Enter a verb: ')
              }


for i in dictionary:
    ml_content = ml_content.replace(i, dictionary[i])

print(ml_content)

file = open('mad_libs_result', 'w')
file.write(ml_content)
file.close()
