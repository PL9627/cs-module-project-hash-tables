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


def walk_graph(graph, distance=5, start_node=None):
    if distance <= 0:
        return []

    if not start_node:
        start_node = random.choice(list(graph.keys()))

    weights = np.array(
        list(markov_graph[start_node].values()),
        dtype=np.float64
    )
    weights /= weights.sum()

    choices = list(markov_graph[start_node].keys())
    chosen_word = np.random.choice(choices, None, p=weights)

    return [chosen_word] + walk_graph(
        graph, distance = distance - 1,
        start_node=chosen_word
    )


for i in range(10):
    print(' '.join(walk_graph(
        markov_graph, distance=12
    )), '\n')
# TODO: analyze which words can follow other words
# Your code here


# TODO: construct 5 random sentences
# Your code here
