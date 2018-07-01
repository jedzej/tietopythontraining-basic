import re


WORDS = ['ADJECTIVE', 'NOUN', 'VERB', 'NOUN']


def mad_libs(adjective, noun, verb, noun2):
    mad_words = [adjective, noun, verb, noun2]
    story = open('story.txt', 'r')
    panda_story = story.read()
    print(len(WORDS))
    for i in range(len(WORDS)):
        story_editor = re.sub(r"\b{}\b".format(WORDS[i]), mad_words[i],
                              panda_story, count=1)
        panda_story = story_editor
    return story_editor


def create_story_file():
    file_story = open('story.txt', 'w')
    story = ('The ADJECTIVE panda walked to the NOUN and'
             ' then VERB. A nearby NOUN was unaffected by these events.')
    file_story.write(story)
    file_story.close()


def main():
    create_story_file()
    user_adjective = input('Enter an adjective: ')
    user_noun = input('Enter a noun: ')
    user_verb = input('Enter a verb: ')
    user_sec_noun = input('Enter second noun: ')
    print(mad_libs(user_adjective, user_noun, user_verb, user_sec_noun))


if __name__ == '__main__':
    main()
