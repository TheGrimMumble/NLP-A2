#!/usr/bin/env python3

"""
NLP A2: N-Gram Language Models

@author: Klinton Bicknell, Harry Eldridge, Nathan Schneider, Lucia Donatelli, Alexander Koller

DO NOT SHARE/DISTRIBUTE SOLUTIONS WITHOUT THE INSTRUCTOR'S PERMISSION
"""

import numpy as np
from sklearn.preprocessing import normalize
from generate import GENERATE
import random
import codecs
import pandas as pd

vocab = codecs.open("brown_vocab_100.txt")

# load the indices dictionary
word_index_dict = {}
for i, line in enumerate(vocab):
    line = line.rstrip()
    word_index_dict[line] = i

f = codecs.open("brown_100.txt")

# initiate matrix with the counts
counts = np.zeros((len(word_index_dict), len(word_index_dict)))

# iterate through file and update counts
for line in f:
    words = line.lower().split()
    previous_word = '<s>'
    for word in words[1:]:
        # add 1 to the counts at the correct index
        index_first_word = word_index_dict[previous_word]
        index_second_word = word_index_dict[word]
        counts[index_first_word, index_second_word] += 1
        previous_word = word

counts += 0.1
print('the:', counts[604,])
print('anonymous:', counts[34,])

# normalize counts
probs = normalize(counts, norm='l1', axis=1)

# writeout bigram probabilities
with open('smooth_probs.txt', 'w') as wf:
    wf.write('p(the | all): ' + str(probs[word_index_dict['all'], word_index_dict['the']]) + '\n')
    wf.write('p(jury | the): ' + str(probs[word_index_dict['the'], word_index_dict['jury']]) + '\n')
    wf.write('p(campaign | the): ' + str(probs[word_index_dict['the'], word_index_dict['campaign']]) + '\n')
    wf.write('p(calls | anonymous): ' + str(probs[word_index_dict['anonymous'], word_index_dict['calls']]))

counts_df = pd.DataFrame(counts)
counts_df.to_csv('counts_smooth.csv')

f.close()