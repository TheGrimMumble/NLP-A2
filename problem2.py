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

print(counts)

probs = counts / np.sum(counts)

with open("unigram_probs.txt", "w") as file:
    file.write(str(probs))

# initialize the joint probabilities of the 2 sentences as 1 and the lenghts to 0
unigram_probs_toy = [1, 1]
sent_len = []
perplexity = []
with open('toy_corpus.txt') as file:
    for i, line in enumerate(file):
        sent_len.append(len(line.split()))
        for word in line.split():
            # get the index of the word and then the probability
            word_index = word_index_dict[word.lower()]
            word_prob = probs[word_index]
            # update the joint probability of this sentence by multiplying it
            unigram_probs_toy[i] *= word_prob
        # compute the perplexity of this sentence
        perplexity.append(1 / pow(unigram_probs_toy[i], 1.0 / sent_len[i]))

# write the perplexities to a text file
with open('unigram_eval.txt', 'w') as wf:
    wf.write(str(perplexity[0]) + '\n')
    wf.write(str(perplexity[1]))

# generate and write 10 sentences to file
with open('unigram_generation.txt', 'w') as wf:
    for i in range(10):
        STR = GENERATE(word_index_dict, probs, "unigram", max_words=20, start_word="<s>")
        wf.write(STR + "\n")