# -*- coding: utf-8 -*-
import collocations_file, collocations_wikipedia
from collocations_common import print_collocations, sort_collocations

collocations = collocations_wikipedia.find('wikipedia_articles')
collocations = collocations_file.find('text3.txt', collocations)
collocations = sort_collocations(collocations)
print_collocations(collocations, 15)
