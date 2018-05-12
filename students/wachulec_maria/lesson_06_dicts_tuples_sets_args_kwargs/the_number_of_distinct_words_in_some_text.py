def distinct_words():
    n = int(input())
    word = set()
    for i in range(n):
        text = set(input().split())
        word.update(text)
    return len(word)


w = distinct_words()
print(w)
