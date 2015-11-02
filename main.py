def trim_word(word):
    if not word:
        return None

    flag = False

    if word[-1:] in ['.', ',', '\'', '\"', '-']:
        word = word[:-1]
        flag = True

    if word and word[0] in ['.', ',', '\'', '\"', '-']:
        word = word[1:]
        flag = True

    if flag:
        word = trim_word(word)

    return word

file = open('text.txt', 'r')

firstWord = None
secondWord = None
thirdWord = None

for line in file:
    for word in line.split():
        firstWord = secondWord
        secondWord = thirdWord
        thirdWord = trim_word(word)

        if secondWord and secondWord not in ['-']:
            pass

# dodatkowa iteracja dla ostatniego slowa
firstWord = secondWord
secondWord = thirdWord
pass
