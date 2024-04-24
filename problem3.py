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

# normalize counts
probs = normalize(counts, norm='l1', axis=1)

# writeout bigram probabilities
with open('bigram_probs.txt', 'w') as wf:
    wf.write('p(the | all): ' + str(probs[word_index_dict['all'], word_index_dict['the']]) + '\n')
    wf.write('p(jury | the): ' + str(probs[word_index_dict['the'], word_index_dict['jury']]) + '\n')
    wf.write('p(campaign | the): ' + str(probs[word_index_dict['the'], word_index_dict['campaign']]) + '\n')
    wf.write('p(calls | anonymous): ' + str(probs[word_index_dict['anonymous'], word_index_dict['calls']]))

f.close()

# initialize the joint probabilities of the 2 sentences as 1
bigram_probs_toy = [1, 1]
n_bigrams = [0, 0]
perplexity = []
with open('toy_corpus.txt') as file:
    for i, line in enumerate(file):
        previous_word = '<s>'
        for word in line.split()[1:]:
            # get the index of the word and then the probability
            word_index = word_index_dict[word.lower()]
            previous_word_index = word_index_dict[previous_word]
            prob = probs[previous_word_index, word_index]
            # update the joint probability of this sentence by multiplying it
            bigram_probs_toy[i] *= prob
            previous_word = word.lower()
            n_bigrams[i] += 1
        # compute the perplexity of this sentence
        perplexity.append(1 / pow(bigram_probs_toy[i], 1.0 / n_bigrams[i]))

# write the perplexities to a text file
with open('bigram_eval.txt', 'w') as wf:
    wf.write(str(perplexity[0]) + '\n')
    wf.write(str(perplexity[1]))

# generate and write 10 sentences to file
with open('bigram_generation.txt', 'w') as wf:
    for i in range(10):
        STR = GENERATE(word_index_dict, probs, "bigram", max_words=20, start_word="<s>")
        wf.write(STR + "\n")