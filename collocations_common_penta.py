
def sort_collocations_penta(collocations):
    collocations_list = []
    for first_word in collocations.keys():
        for second_word in collocations[first_word].keys():
            for third_word in collocations[first_word][second_word].keys():
                for fourth_word in collocations[first_word][second_word][third_word].keys():
                    for fifth_word in collocations[first_word][second_word][third_word][fourth_word].keys():
                        collocations_list.append((first_word, second_word, third_word, fourth_word, fifth_word, collocations[first_word][second_word][third_word][fourth_word][fifth_word]))
    collocations_list = sorted(collocations_list, key=lambda collocation: collocation[5], reverse=True)
    return collocations_list


def print_collocations_penta(collocations, number):
    for c in collocations[:number]:
        print c[0], c[1], c[2], c[3], c[4], c[5]


def print_collocations_for_test_area_penta(collocations, number):
    text = ''
    for c in collocations[:number]:
        text += '{0} {1} {2} {3} {4} {5}\n'.format(c[0], c[1], c[2], c[3], c[4], c[5])
    return text

def count_collocations_penta(collocations, first_word, second_word, third_word, fourth_word, fifth_word):
    if first_word and second_word and third_word and fourth_word and fifth_word and first_word not in ['-'] and second_word not in ['-'] and third_word not in ['-'] and fourth_word not in ['-'] and fifth_word not in ['-']:
        if first_word not in collocations.keys():
            collocations[first_word] = dict()

        if second_word not in collocations[first_word].keys():
            collocations[first_word][second_word] = dict()
       
        if third_word not in collocations[first_word][second_word].keys():
            collocations[first_word][second_word][third_word] = dict()

        if fourth_word not in collocations[first_word][second_word][third_word].keys():
            collocations[first_word][second_word][third_word][fourth_word] = dict()

        if fourth_word not in collocations[first_word][second_word][third_word][fourth_word].keys():
            collocations[first_word][second_word][third_word][fourth_word][fifth_word] = 1

        else:
            collocations[first_word][second_word][third_word][fourth_word][fifth_word] +=1

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
