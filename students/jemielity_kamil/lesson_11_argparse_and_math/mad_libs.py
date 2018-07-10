import argparse


parser = argparse.ArgumentParser(description='Short sample app')
parser.add_argument('-adj', action='store',
                    dest="adjective", required=True,
                    help='Adjective')

parser.add_argument('-n', action="store",
                    dest='noun', required=True,
                    help="Noun")

parser.add_argument('-adv', action="store",
                    dest='adverb', required=True,
                    help="Adverb")

parser.add_argument('-v', action="store",
                    dest='verb', required=True,
                    help="Verb")


args = parser.parse_args()

mad_libs_file = open('mad_libs')
mad_libs_content = mad_libs_file.read()
mad_libs_file.close()

dictionary = {'ADJECTIVE': args.adjective,
              'NOUN': args.noun,
              'ADVERB': args.adverb,
              'VERB': args.verb
              }

for i in dictionary:
    mad_libs_content = mad_libs_content.replace(i, dictionary[i])

print(mad_libs_content)

file = open('mad_libs_result', 'w')
file.write(mad_libs_content)
