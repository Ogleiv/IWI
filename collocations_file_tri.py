from collocations_common_tri import count_collocations_tri, trim_word
from stemming.porter2 import stem


def find_collocations_tri(file_name, data, popular_word):
    text_file = open(file_name, 'r')
    file_content = text_file.read()

    most_common_words = find_most_common_words(file_content, popular_word)

    second_word = None
    third_word = None
    fourth_word = None
    collocations = data

    text_file.seek(0)
    for line in text_file:
        for word in line.split():
            first_word = second_word
            second_word = third_word
            third_word = fourth_word
            fourth_word = trim_word(word)
            if (first_word not in most_common_words and second_word not in most_common_words and third_word not in most_common_words) and \
                    (first_word and first_word[0].islower() and second_word and second_word[0].islower() and third_word and third_word[0].islower()):
                count_collocations_tri(collocations, stem(first_word.lower()), stem(second_word.lower()), stem(third_word.lower()))

    #dodatkowa iteracja dla ostatniego slowa
    first_word = second_word
    second_word = third_word
    third_word = fourth_word                                   
    count_collocations_tri(collocations, first_word, second_word, third_word)
    return collocations, most_common_words, file_content


def find_most_common_words(text, count):
    words = dict()
    for word in text.split():
        word = trim_word(word)
        if word not in words.keys():
            words[word] = 1
        else:
            words[word] += 1
    sorted_words = sorted(words, key=words.get, reverse=True)
    return sorted_words[:count]


def find(file_name, data=None):
    if data:
        collocations = data
    else:
        collocations = dict()
    return find_collocations_tri(file_name, collocations)
