
text_file = open('../lesson_09_reading_and_writing_files/file.txt')

text_to_work = text_file.read()

# text_to_work = text_to_work.split()

print(text_to_work)

adj = input('Enter an adjective: ')  # silly
noun = input('Enter a noun: ')       # chandelier
verb = input('Enter a verb: ')       # screamed
adv = input('Enter an adverb: ')     # quickly

text_to_work = text_to_work.replace('ADJECTIVE', str(adj))
text_to_work = text_to_work.replace('NOUN', noun)
text_to_work = text_to_work.replace('VERB', verb)
text_to_work = text_to_work.replace('ADVERB', adv)

print(text_to_work)
result_file = open('../lesson_09_reading_and_writing_files/result.txt', 'w')
result_file.write(str(text_to_work))
