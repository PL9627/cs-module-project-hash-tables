import random
import numpy as np
import re
from collections import defaultdict

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()
tokenized_text = [
    word for word in re.split('\W+', words)
    if word != ''
]

markov_graph = defaultdict(lambda: defaultdict(int))

last_word = tokenized_text[0].lower()
for word in tokenized_text[1:]:
    word = word.lower()
    markov_graph[last_word][word] += 1
    last_word = word

""" limit = 3
for first_word in ('the', 'by', 'who'):
    next_words = list(markov_graph[first_word].keys())[:limit]
    for next_word in next_words:
        print(first_word, next_word)
 """

def walk_graph(graph, distance = 5, start_node = None):
    pass
# TODO: analyze which words can follow other words
# Your code here


# TODO: construct 5 random sentences
# Your code here

