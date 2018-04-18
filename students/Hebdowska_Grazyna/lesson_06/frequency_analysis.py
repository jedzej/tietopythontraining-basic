from operator import itemgetter


def insert_text(n):
    new_text = []
    for i in range(n):
        new_ = input()
        new_ = new_.split(' ')
        new_text.append(new_)
    return new_text


def frequency(some_text):
    frequwncy = {}
    for i in some_text:
        for j in i:
            if j not in frequwncy.keys():
                frequwncy[j] = 1
            else:
                frequwncy[j] += 1
    return frequwncy


def frequency_analisys(freq):
    analysis = []
    for i in freq.keys():
        analysis.append((freq[i], i))
    result = sorted(analysis, key=itemgetter(0, 1))
    return result


def print_analyzis(analysis):
    for i in analysis:
        print(i[1])


number_of_lines = int(input("Number of text lines: "))
a_text = insert_text(number_of_lines)
print_analyzis(frequency_analisys(frequency(a_text)))
