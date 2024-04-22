from nltk.corpus import brown
from nltk.tokenize import word_tokenize
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
import time


def unique_words_by_frequency(input_word_list):
    all_lower_case = [w.lower() for w in input_word_list]
    frequency_counter = Counter(all_lower_case)
    return sorted(frequency_counter.items(), key=lambda value: value[1], reverse=True)


def plot_zipfs_law(input_data, log_log=False):
    x, y = zip(*input_data)
    if log_log:
        x = np.log(np.arange(1, int(len(x)) + 1))
        y = np.log(np.array(y))
    plt.plot(x, y, linestyle='-', linewidth=2)
    plt.xticks([])
    plt.title("Zipf's Law")
    plt.xlabel("Position in list")
    plt.ylabel("Word-frequencies")
    plt.show()


def test_process_time():
    start = time.time()
    # paste test function here
    end = time.time()
    print(f'Processing time: {end - start}')


def collect_data(WORDS=False, SENTENCES=False):
    if WORDS:
        corpus_words = list(brown.words())
        word_frequencies = unique_words_by_frequency(corpus_words)
        mean_word_length = sum([len(w) for w in corpus_words]) / len(corpus_words)
        return word_frequencies, len(word_frequencies), len(corpus_words), \
                round(mean_word_length, 2)
    if SENTENCES:
        corpus_sentences = list(brown.sents())
        all_corpus_sents = [' '.join(corpus_sentences[i]) for i in range(len(corpus_sentences))]
        tokens = [word_tokenize(s) for s in all_corpus_sents]
        mean_words_per_sent = sum([len(w) for w in corpus_sentences]) / len(corpus_sentences)
        # run default part of speech tagger, id ten most frequent POS tags
        POS_tags = "MISSING! NEED TO IMPLEMENT THIS CODE"
        return len(tokens), round(mean_words_per_sent, 2), POS_tags


word_frequencies, unique_words, sum_all_words, average_word_len = collect_data(WORDS=True)
sum_tokens, average_words_per_sent, POS_tags = collect_data(SENTENCES=True)

info_text = f'Number of unique words: {unique_words}\nTotal number of words: {sum_all_words}\n' \
        f'Average word length: {average_word_len}\nNumber of Tokens: {sum_tokens}\n' \
        f'Average number of words per sentence: {average_words_per_sent}' \
        f'Ten most frequent POS tags: {POS_tags}'

print(info_text)
plot_zipfs_law(word_frequencies)
plot_zipfs_law(word_frequencies, log_log=True)


"""
What counts as words? E.g. "It's", "September-October", "Full-time"
"""