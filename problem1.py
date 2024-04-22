#!/usr/bin/env python3

"""
NLP A2: N-Gram Language Models

@author: Klinton Bicknell, Harry Eldridge, Nathan Schneider, Lucia Donatelli, Alexander Koller

DO NOT SHARE/DISTRIBUTE SOLUTIONS WITHOUT THE INSTRUCTOR'S PERMISSION
"""

word_index_dict = {}

# read brown_vocab_100.txt into word_index_dict
with open("brown_vocab_100.txt") as file:
    for i, word in enumerate(file):
        word = word.rstrip()
        word_index_dict[word] = i

# write word_index_dict to word_to_index_100.txt
with open("word_to_index.txt", "w") as file:
    file.write(str(word_index_dict))

print(word_index_dict['all'])
print(word_index_dict['resolution'])
print(len(word_index_dict))
