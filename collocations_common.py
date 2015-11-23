def sort_collocations(collocations):
    collocations_list = []
    for first_word in collocations.keys():
        for second_word in collocations[first_word].keys():
            collocations_list.append((first_word, second_word, collocations[first_word][second_word]))
    collocations_list = sorted(collocations_list, key=lambda collocation: collocation[2], reverse=True)
    return collocations_list


def print_collocations(collocations, number):
    for c in collocations[:number]:
        print c[0], c[1], c[2]


def count_collocations(collocations, first_word, second_word):
    if first_word and second_word and first_word not in ['-'] and second_word not in ['-']:
        if first_word not in collocations.keys():
            collocations[first_word] = dict()

        if second_word not in collocations[first_word].keys():
            collocations[first_word][second_word] = 1
        else:
            collocations[first_word][second_word] += 1


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