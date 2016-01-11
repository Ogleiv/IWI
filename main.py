# -*- coding: utf-8 -*-
import collocations_file, collocations_wikipedia
import collocations_file_tri, collocations_wikipedia_tri
import collocations_file_tetra, collocations_wikipedia_tetra
import collocations_file_penta 
from collocations_common_penta import print_collocations_penta, sort_collocations_penta
from collocations_common_tetra import print_collocations_tetra, sort_collocations_tetra
from collocations_common_tri import print_collocations_tri, sort_collocations_tri
from collocations_common import print_collocations, sort_collocations
print "--------------------------"
print "Lista kolokacji (2 wyrazy)"
print "--------------------------"
#kolokacja - 2 wyrazy
#collocations = collocations_wikipedia.find('wikipedia_articles')
collocations = collocations_file.find('text3.txt', dict())
collocations = sort_collocations(collocations)
print_collocations(collocations, 50)
print "--------------------------"
print "Lista kolokacji (3 wyrazy)"
print "--------------------------"
#kolokacja - 3 wyrazy
#collocations = collocations_wikipedia_tri.find('wikipedia_articles')
collocations = collocations_file_tri.find('text3.txt',dict())
collocations = sort_collocations_tri(collocations)
print_collocations_tri(collocations, 50)
print "--------------------------"
print "Lista kolokacji (4 wyrazy)"
print "--------------------------"
#kolokacja - 4 wyrazy
#collocations = collocations_wikipedia_tetra.find('wikipedia_articles')
collocations = collocations_file_tetra.find('text3.txt',dict())
collocations = sort_collocations_tetra(collocations)
print_collocations_tetra(collocations, 50)
print "--------------------------"
print "Lista kolokacji (5 wyrazow)"
print "--------------------------"
#kolokacja - 4 wyrazy
#collocations = collocations_wikipedia_penta.find('wikipedia_articles')
collocations = collocations_file_penta.find('text3.txt',dict())
collocations = sort_collocations_penta(collocations)
print_collocations_penta(collocations, 20)

