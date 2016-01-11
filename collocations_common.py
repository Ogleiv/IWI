from stemming.porter2 import stem


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


def print_collocations_for_test_area(collocations, number):
    text = ''
    for c in collocations[:number]:
        text += '{0} {1} {2}\n'.format(c[0], c[1], c[2])

    return text


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


def get_collocatios_from_string_2(text, data):

    most_common_words = find_most_common_words(text, 10)

    second_word = None
    third_word = None
    collocations = data

    # text.seek(0)
    for word in text.split():
        first_word = second_word
        second_word = third_word
        third_word = trim_word(word)
        if (first_word not in most_common_words and second_word not in most_common_words) and \
                (first_word and first_word[0].islower() and second_word and second_word[0].islower()):
            count_collocations(collocations, stem(first_word.lower()), stem(second_word.lower()))

    # dodatkowa iteracja dla ostatniego slowa
    first_word = second_word
    second_word = third_word
    count_collocations(collocations, first_word, second_word)
    return collocations, most_common_words


def find_most_common_words(text_file, count):
    words = dict()
    for line in text_file:
        for word in line.split():
            word = trim_word(word)
            if word not in words.keys():
                words[word] = 1
            else:
                words[word] += 1
    sorted_words = sorted(words, key=words.get, reverse=True)
    return sorted_words[:count]
