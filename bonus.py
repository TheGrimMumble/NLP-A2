from collections import Counter
import numpy as np


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


corpus = load_corpus('brown_100.txt')
vocabulary, vocabulary_with_counts = find_filtered_vocabulary(corpus)
word_pair_list = find_word_pairs(corpus, vocabulary)
full_pmi_list = pmi(word_pair_list, vocabulary_with_counts, len(corpus))
sorted_pmi = sorted(full_pmi_list.items(), key=lambda pmi: pmi[1], reverse=True)
twenty_highest = sorted_pmi[:20]
twenty_lowest = sorted_pmi[-20:]
print(twenty_highest)
print(len(twenty_highest))
print(twenty_lowest)
print(len(twenty_lowest))


"""
Are we supposed to run it on the FULL brown corpus or only brown_100.txt?
"""
