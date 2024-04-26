from collections import Counter
import numpy as np
from nltk.corpus import brown


def load_corpus(corpus_file):
    corpus = []
    with open(corpus_file) as text:
        for sentence in text:
            for word in sentence.lower().split():
                corpus.append(word)
    return corpus


def find_filtered_vocabulary(input_corpus):
    vocabulary_with_counts = {word: count for word, count in Counter(input_corpus).items() if count >= 10}
    sort = sorted(vocabulary_with_counts.items(), key=lambda count: count[1], reverse=True)
    vocabulary = [word for word, count in sort]
    return vocabulary, vocabulary_with_counts


def find_word_pairs(input_corpus, vocabulary):
    successive_word_pairs = []
    for i in range(len(input_corpus) - 1):
        if input_corpus[i] in vocabulary and input_corpus[i + 1] in vocabulary:
            successive_word_pairs.append((input_corpus[i], input_corpus[i + 1]))
    word_pair_frequency = Counter(successive_word_pairs)
    return word_pair_frequency


def pmi(word_pair_dict, word_frequencies, corpus_len):
    word_pair_pmi = {}
    for k in word_pair_dict:
        word_pair_pmi[k] = round(np.log((word_pair_dict[k] * corpus_len) / (word_frequencies[k[0]] * word_frequencies[k[1]])), 3)
    return word_pair_pmi


corpus = list(brown.words())
vocabulary, vocabulary_with_counts = find_filtered_vocabulary(corpus)
word_pair_list = find_word_pairs(corpus, vocabulary)
full_pmi_list = pmi(word_pair_list, vocabulary_with_counts, len(corpus))
sorted_pmi = sorted(full_pmi_list.items(), key=lambda pmi: pmi[1], reverse=True)
twenty_high_low = (('20 Word Pairs with Highest PMI:\n', sorted_pmi[:20]), ('\n20 Word Pairs with Lowest PMI:\n', sorted_pmi[-20:]))

with open("pmi_high_low.txt", "w") as file:
    for high_low in twenty_high_low:
        file.write(high_low[0])
        file.write(f'{"Word Pair:":<24}PMI:\n')
        for word_pair_pmi in high_low[1]:
            info = f'{str(word_pair_pmi[0]):<24}{word_pair_pmi[1]}\n'
            file.write(info)

"""
Are we supposed to run it on the FULL brown corpus or only brown_100.txt? - probably the whole corpus

Are we supposed to just use the counts of the word pairs and words in the equation (i.e. use the approximation)? - it is good

Are we supposed to take the absolute value of pmi, or leave in the negative values? - include negative
"""
