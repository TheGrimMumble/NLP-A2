from nltk.corpus import brown
from nltk.tokenize import sent_tokenize
import matplotlib, re, time

print(len(brown.words()))

for k in range(1, 4):
    start = time.time()
    length = 10 ** k
    dic = {brown.words()[i]: 0 for i in range(length)}
    for i in range(length):
        dic[brown.words()[i]] += 1
    final = sorted(dic.items(), key=lambda value: value[1], reverse=True)
    end = time.time()
    print(final[0], f'Time:{end - start}')

def unique_words_by_frequency(corpus_sentences, only_words=True):
    word_def = re.compile("^[a-zA-Z]+[\-']*$")
    for i in range(20):
        for j in corpus_sentences[i]:
            if word_def.fullmatch(corpus_sentences[i][j]):
                print(corpus_sentences[i][j])
            else:
                print(f'not accepted:{corpus_sentences[i][j]}')
    if only_words:
        # give only a list of ordered words
        pass
    if not only_words:
        # give: list of ordered words, list of respective frequency, dictionary of information
        pass

"""
what about it's, september-october, capital letters?

"""


def plot_zipfs_law(input_data, log_log=False):
    pass


#unique_words_by_frequency(brown.sents())