# -*- coding: utf-8 -*-


def trim_word(word):
    if not word:
        return None

    flag = False

    if word[-1:] in ['.', ',', '\'', '\"', '-', '—']:
        word = word[:-1]
        flag = True

    if word and word[0] in ['.', ',', '\'', '\"', '-', '—']:
        word = word[1:]
        flag = True

    if flag:
        word = trim_word(word)

    return word


def count_collocations(collocations, firstWord, secondWord):
    if firstWord and secondWord and firstWord not in ['—'] and secondWord not in ['—']:
        if not collocations.has_key(firstWord):
            collocations[firstWord] = dict()

        if not collocations[firstWord].has_key(secondWord):
            collocations[firstWord][secondWord] = 1
        else:
            collocations[firstWord][secondWord] += 1


def sort_collocations(collocations):
    collocations_list = []
    for first_word in collocations.keys():
        for second_word in collocations[first_word].keys():
           collocations_list.append((first_word, second_word, collocations[first_word][second_word]))
    collocations_list = sorted(collocations_list, key=lambda collocation: collocation[2], reverse=True)

    for c in collocations_list[:10]:
        print c[0], c[1], c[2]

file = open('text.txt', 'r')

firstWord = None
secondWord = None
thirdWord = None

collocations = dict()

for line in file:
    for word in line.split():
        firstWord = secondWord
        secondWord = thirdWord
        thirdWord = trim_word(word)
        count_collocations(collocations, firstWord, secondWord)

# dodatkowa iteracja dla ostatniego slowa
firstWord = secondWord
secondWord = thirdWord
count_collocations(collocations, firstWord, secondWord)

sort_collocations(collocations)


