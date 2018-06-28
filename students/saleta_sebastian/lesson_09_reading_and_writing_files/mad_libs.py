def mad_libs(adjective, noun, verb, noun2):
    file_story = open('story.txt', 'w')
    story = ('The {} panda walked to the {} and then {}. A nearby {} '
             'was unaffected by these events.'
             .format(adjective, noun, verb, noun2))
    file_story.write(story)
    file_story.close()

    return story


def main():
    user_adjective = input('Enter an adjective: ')
    user_noun = input('Enter a noun: ')
    user_verb = input('Enter a verb: ')
    user_sec_noun = input('Enter second noun: ')
    print(mad_libs(user_adjective, user_noun, user_verb, user_sec_noun))


if __name__ == '__main__':
    main()
