from nltk.corpus import brown
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
import time


def plot_zipfs_law(genre, input_data, log_log=False):
    plot_file_name = 'zipf_plot_' + str(genre)
    plot_title = f"Zipf's Law | Genre: {genre}"
    x, y = zip(*input_data)
    if log_log:
        x = np.log(np.arange(1, int(len(x)) + 1))
        y = np.log(np.array(y))
        plot_file_name += '_log_log'
        plot_title += ' | Log(x) Log(y) Plot'
    plt.plot(x, y, linestyle='-', linewidth=2)
    plt.xticks([])
    plt.title(plot_title)
    plt.xlabel("Position in list")
    plt.ylabel("Word-frequencies")
    plt.savefig(f'{plot_file_name}.png')
    plt.close()


def collect_data(genre, WORDS=False, SENTENCES=False):
    if WORDS:
        # prepare list of all words in lower-case
        corpus_words = list(brown.words(categories=genre))
        corpus_lower_case = [w.lower() for w in corpus_words]

        # calculate mean word length, make word frequency list and list of all tokens
        average_word_length = sum([len(w) for w in corpus_words]) / len(corpus_words)
        word_frequency_count = sorted(Counter(corpus_lower_case).items(), key=lambda count: count[1], reverse=True)
        corpus_tokens = word_tokenize(' '.join(corpus_lower_case))

        # find 10 most frequent POS tags
        PartOfSpeech = pos_tag(corpus_tokens)
        POS_words, POS_tags = zip(*PartOfSpeech)
        ten_most_frequent_POS = sorted(Counter(POS_tags).items(), key=lambda count: count[1], reverse=True)[0:10]

        return word_frequency_count, len(word_frequency_count), len(corpus_words), \
                round(average_word_length, 2), len(corpus_tokens), ten_most_frequent_POS
    
    if SENTENCES:
        # prepare list of all corpus sentences and calculate mean words per sentence
        corpus_sentences = list(brown.sents(categories=genre))
        average_words_per_sent = sum([len(w) for w in corpus_sentences]) / len(corpus_sentences)

        return round(average_words_per_sent, 2)


def test_process_time():
    start = time.time()

    # paste test function here
    example_function = collect_data('science_fiction', SENTENCES=True)

    end = time.time()
    print(f'Processing time: {end - start}')


genres = [None, 'humor', 'science_fiction']

with open("zipfs_law_info.txt", "w") as file:
    for genre in genres:
        word_frequencies, types_ie_unique_words, sum_all_words, average_word_length, sum_tokens, POS_tags \
            = collect_data(genre, WORDS=True)
        average_words_per_sent = collect_data(genre, SENTENCES=True)
        info_text = f'Genre: {genre}\n' \
                f'Number of types (unique words): {types_ie_unique_words}\nTotal number of words: {sum_all_words}\n' \
                f'Average word length: {average_word_length}\nNumber of Tokens: {sum_tokens}\n' \
                f'Average number of words per sentence: {average_words_per_sent}\n' \
                f'Ten most frequent POS tags (POS, count):\n{POS_tags}\n\n'
        file.write(info_text)
        plot_zipfs_law(genre, word_frequencies)
        plot_zipfs_law(genre, word_frequencies, log_log=True)

