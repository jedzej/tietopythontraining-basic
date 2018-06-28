def distinct_words():
    a = int(input())
    word = set()
    for i in range(a):
        text = set(input().split())
        word.update(text)
    return len(word)


print(distinct_words())
