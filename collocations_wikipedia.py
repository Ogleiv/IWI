from collocations_common import count_collocations, trim_word, find_whole_collocations_from_stems
from stemming.porter2 import stem
import wikipedia


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


def find_collocations(text, data, popular_word):

    most_common_words = find_most_common_words(text, popular_word)

    second_word = None
    third_word = None

    collocations = data
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

    collocations = find_whole_collocations_from_stems(collocations, text)
    return collocations, most_common_words


def get_article_from_wikipedia(title):
    try:
        wiki = wikipedia.page(title)
    except Exception as e:
        return False, e

    return True, wiki


def single_article(title):
    wiki = wikipedia.page(title)
    return find_collocations(wiki.content, dict())


def find(file_name, data=None):
    if data:
        collocations = data
    else:
        collocations = dict()
    articles = open(file_name, 'r')
    for article in articles:
        wiki = wikipedia.page(article)
        collocations = find_collocations(wiki.content, collocations)
    return collocations
