from nltk.corpus import brown
from nltk.tokenize import sent_tokenize, word_tokenize
from collections import Counter
import matplotlib, re, time


def unique_words_by_frequency(input_word_list):
    all_lower_case = [w.lower() for w in input_word_list]
    frequency_counter = Counter(all_lower_case)
    return sorted(frequency_counter.items(), key=lambda value: value[1], reverse=True)


def get_info(sentences):
    all_corpus_sents = [' '.join(sentences[i]) for i in range(len(sentences))]
    tokens = [word_tokenize(s) for s in all_corpus_sents]
    mean_words_per_sent = sum([len(w) for w in sentences]) / len(sentences)
    # run default part of speech tagger, id ten most frequent POS tags
    return f'Number of Tokens: {len(tokens)}/n' \
            f'Average number of words per sentence: {mean_words_per_sent}'


def plot_zipfs_law(input_data, log_log=False):
    pass


def test_process_time():
    start = time.time()
    # paste function here
    end = time.time()
    print(f'Processing time: {end - start}')


def collect_data(WORDS=False, SENTENCES=False):
    if WORDS:
        corpus_words = list(brown.words())
        mean_word_length = sum([len(w) for w in corpus_words]) / len(corpus_words)
        word_frequencies = unique_words_by_frequency(corpus_words)
        return word_frequencies, len(word_frequencies), len(corpus_words), \
                mean_word_length
    if SENTENCES:
        corpus_sentences = list(brown.sents())
        info = get_info(corpus_sentences)
        return info

#word_frequencies, unique_words, sum_all_words, average_word_len = 
print(collect_data(WORDS=True))


"""
what about it's, september-october, capital letters?
"""