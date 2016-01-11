# -*- coding: utf-8 -*-

import collocations_file, collocations_wikipedia
import collocations_file_tri, collocations_wikipedia_tri
import collocations_file_tetra, collocations_wikipedia_tetra
import collocations_file_penta, collocations_wikipedia_penta
from collocations_common_penta import sort_collocations_penta, print_collocations_for_test_area_penta
from collocations_common_tetra import sort_collocations_tetra, print_collocations_for_test_area_tetra
from collocations_common_tri import sort_collocations_tri, print_collocations_for_test_area_tri
from collocations_common import sort_collocations, print_collocations_for_test_area
from Tkinter import *
import Tkinter as tk
import ttk
from tkFileDialog import askopenfilename


class Main(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        self.frame = tk.Frame(self)
        self.option_frame = tk.Frame(self.frame)
        self.notebook_frame = tk.Frame(self.frame)

        self.global_option_frame = ttk.LabelFrame(self.option_frame, text='Options')
        self.wikipedia_frame = ttk.LabelFrame(self.option_frame, text='Wikipedia')
        self.file_frame = ttk.LabelFrame(self.option_frame, text='File')

        self.collocation_words = StringVar(self.option_frame)
        self.collocation_words.set('2')

        self.label_article = tk.Label(self.wikipedia_frame, text='Find single article')
        self.entry1 = tk.Entry(self.wikipedia_frame)
        self.button_article = tk.Button(self.wikipedia_frame, text="Find article", command=lambda: self.wikipedia_article())

        self.label_file = tk.Label(self.file_frame, text='Find collocations in file')
        self.button_file = tk.Button(self.file_frame, text='Choose file and find', command=lambda: self.file_read())

        self.words_label = tk.Label(self.global_option_frame, text='Numer of words:')
        self.words_options = OptionMenu(self.global_option_frame, self.collocation_words, '2', '3', '4', '5')

        self.ignore_label = tk.Label(self.global_option_frame, text='Popular words to ignore:')
        self.ignore_entry = tk.Entry(self.global_option_frame, text='10')

        self.global_option_frame.pack(padx=1, pady=1, side=TOP, fill=X)
        self.wikipedia_frame.pack(padx=1, pady=1, side=TOP, fill=X)
        self.file_frame.pack(padx=1, pady=1, side=TOP, fill=X)

        self.label_article.pack(padx=2, pady=2)
        self.entry1.pack(padx=1, pady=1)
        self.button_article.pack(fill=X, padx=1, pady=1)
        self.label_file.pack(padx=1, pady=10)
        self.button_file.pack(padx=1, pady=0, fill=X)
        self.words_label.pack(padx=1, pady=0)
        self.words_options.pack(padx=1, pady=0, fill=X)
        self.ignore_label.pack(padx=1, pady=0)
        self.ignore_entry.pack(padx=1, pady=0, fill=X)

        self.n = ttk.Notebook(self.notebook_frame)

        self.frame_results = tk.Frame(self.frame)
        self.frame_text = tk.Frame(self.frame)
        self.frame_results.pack()

        self.results = tk.Text(self.frame_results)
        self.results.pack()

        self.article_textarea = tk.Text(self.frame_text)
        self.article_textarea.pack()

        self.n.add(self.frame_results, text='Best Colocations')
        self.n.add(self.frame_text, text='Text')
        self.n.pack()

        self.notebook_frame.pack(side=RIGHT)
        self.option_frame.pack(side=TOP, padx=5, pady=5)
        self.frame.pack()
        self.frame.focus_set()

    def wikipedia_article(self):
        self.results.delete('1.0', END)
        self.article_textarea.delete('1.0', END)
        popular_words = int(self.ignore_entry.get())
        article_text = collocations_wikipedia.get_article_from_wikipedia(self.entry1.get())

        if self.collocation_words.get() == '2':
            collocations, most_common_words = collocations_wikipedia.find_collocations(article_text, dict(), popular_words)
            collocations = sort_collocations(collocations)
            text = print_collocations_for_test_area(collocations, 15)
        elif self.collocation_words.get() == '3':
            collocations, most_common_words = collocations_wikipedia_tri.find_collocations_tri(article_text, dict(), popular_words)
            collocations = sort_collocations_tri(collocations)
            text = print_collocations_for_test_area_tri(collocations, 15)
        elif self.collocation_words.get() == '4':
            collocations, most_common_words = collocations_wikipedia_tetra.find_collocations_tetra(article_text, dict(), popular_words)
            collocations = sort_collocations_tetra(collocations)
            text = print_collocations_for_test_area_tetra(collocations, 15)
        elif self.collocation_words.get() == '5':
            collocations, most_common_words = collocations_wikipedia_penta.find_collocations_penta(article_text, dict(), popular_words)
            collocations = sort_collocations_penta(collocations)
            text = print_collocations_for_test_area_penta(collocations, 15)

        self.results.insert(END, text)
        self.article_textarea.insert(END, article_text)
        

    def file_read(self):
        self.results.delete('1.0', END)
        self.article_textarea.delete('1.0', END)
        popular_words = int(self.ignore_entry.get())
        filename = askopenfilename()

        if self.collocation_words.get() == '2':
            collocations, most_common_words, file_text = collocations_file.find_collocations(filename, dict(), popular_words)
            collocations = sort_collocations(collocations)
            text = print_collocations_for_test_area(collocations, 15)
        elif self.collocation_words.get() == '3':
            collocations, most_common_words, file_text = collocations_file_tri.find_collocations_tri(filename, dict(), popular_words)
            collocations = sort_collocations_tri(collocations)
            text = print_collocations_for_test_area_tri(collocations, 15)
        elif self.collocation_words.get() == '4':
            collocations, most_common_words, file_text = collocations_file_tetra.find_collocations_tetra(filename, dict(), popular_words)
            collocations = sort_collocations_tetra(collocations)
            text = print_collocations_for_test_area_tetra(collocations, 15)
        elif self.collocation_words.get() == '5':
            collocations, most_common_words, file_text = collocations_file_penta.find_collocations_penta(filename, dict(), popular_words)
            collocations = sort_collocations_penta(collocations)
            text = print_collocations_for_test_area_penta(collocations, 15)

        self.results.insert(END, text)
        self.article_textarea.insert(END, file_text)


app = Main()
app.mainloop()


