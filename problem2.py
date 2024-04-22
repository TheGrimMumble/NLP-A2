#!/usr/bin/env python3

"""
NLP A2: N-Gram Language Models

@author: Klinton Bicknell, Harry Eldridge, Nathan Schneider, Lucia Donatelli, Alexander Koller

DO NOT SHARE/DISTRIBUTE SOLUTIONS WITHOUT THE INSTRUCTOR'S PERMISSION
"""

import numpy as np
from generate import GENERATE


vocab = "brown_vocab_100.txt"
word_index_dict = {}

# read brown_vocab_100.txt into word_index_dict
with open(vocab) as file:
    for i, word in enumerate(file):
        word = word.rstrip()
        word_index_dict[word] = i

# initialize counts to a zero vector
counts = np.zeros(len(word_index_dict))

# iterate through file and update counts
with open("brown_100.txt") as text:
    for s in text:
        for w in s.split():
            current_word = w.lower()
            counts[word_index_dict[current_word]] += 1

# print and normalize counts.
print(counts)

probs = counts / np.sum(counts)

with open("unigram_probs.txt", "w") as file:
    file.write(str(probs))
